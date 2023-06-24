

def get_number(i):
    global code
    digits = "0123456789"

    assert code[i] in digits, "\n  <LineCode Error Systeme>\n   Error char "+str(i)+": '"+ code[i] + "'\n   Expected a digit after '" + code[i-1] + "'"

    k = int(code[i])
    size = 1

    while code[i+size] in digits:
        k *= 10
        k += int(code[i+size])
        size += 1
    
    return (k, size)



def calc(i):
    global code
    global var_values
    global var_types
    targets = "nzudvcst+-*/^~%\=<>!&|"

    assert code[i] in targets, "\n  <LineCode Error Systeme>\n   Error char "+str(i)+": '"+ code[i] + "'\n   Expected a value or an operation (starting with '"+targets+"')"

    if code[i] == 'n':
        k = get_number(i+1)
        return ('n', k[0], 1+k[1])

    if code[i] == 'z':
        k = get_number(i+1)
        return ('n', -k[0], 1+k[1])

    if code[i] == 'u':
        k = get_number(i+1)
        return ('u', k[0], 1+k[1])

    if code[i] == 'd':
        interger_part = get_number(i+1)
        symbol_position = i+1+interger_part[1]
        assert code[symbol_position] in "nz", "\n  <LineCode Error Systeme>\n   Error char "+str(symbol_position)+": '"+ code[symbol_position] + "'\n   Expected n or z to signal the symbol of the decimal number"
        decimal_part = get_number(i+2+interger_part[1])
        value = interger_part[0]+float(decimal_part[0])/(10**decimal_part[1])
        if symbol_position == 'z': return('d', -value, 2+interger_part[1]+decimal_part[1])
        return('d', value, 2+interger_part[1]+decimal_part[1])
    
    if code[i] == 'v':
        assert code[i+1] in var_types.keys(), "\n  <LineCode Error Systeme>\n   Error char "+str(i+1)+": '"+ code[i+1] + "'\n   Unknown variable " + code[i+1]
        assert code[i+1] in var_values.keys(), "\n  <LineCode Error Systeme>\n   Error char "+str(i+1)+": '"+ code[i+1] + "'\n   Unset variable " + code[i+1]
        return (var_types[code[i+1]], var_values[code[i+1]], 2)

    if code[i] == 'c':
        return ('c', code[i+1], 2)
    
    if code[i] == 's':
        i += 1
        assert code[i] in 'sl', "\n  <LineCode Error Systeme>\n   Error char "+str(i)+": '"+ code[i] + "'\n   Expected a special caracter target (s or l) after the 'special character' target (s)"
        if code[i] == 's': return('c', ' ', 2)
        return('c', '\n', 2)
    
    if code[i] == 't':
        a = calc(i+1)
        return ('t', a[0], 1+a[2])
    
    if code[i] == '+':
        a = calc(i+1)
        assert a[0] in 'und', "\n  <LineCode Error Systeme>\n   Error chars "+str(i+1)+": '"+ code[i+1:i+1+a[2]] + "'\n   Expected a numeral value in the first element of an addition (+)\n   '" + a[0] + "' type value given"
        b = calc(i+1+a[2])
        assert b[0] in 'und', "\n  <LineCode Error Systeme>\n   Error chars "+str(i+1+a[2])+": '"+ code[i+1+a[2]:i+1+a[2]+b[2]] + "'\n   Expected a numeral value in the second element of an addition (+)\n   '" + b[0] + "' type value given"
        if a[0] == 'd' or b[0] == 'd': 
            return('d', a[1]+b[1], 1+a[2]+b[2])
        if a[0] == 'u' and b[0] == 'u': 
            return('u', a[1]+b[1], 1+a[2]+b[2])
        return('n', a[1]+b[1], 1+a[2]+b[2])
    
    if code[i] == '-':
        a = calc(i+1)
        assert a[0] in 'und', "\n  <LineCode Error Systeme>\n   Error chars "+str(i+1)+": '"+ code[i+1:i+1+a[2]] + "'\n   Expected a numeral value in the first element of a substraction (-)\n   '" + a[0] + "' type value given"
        b = calc(i+1+a[2])
        assert b[0] in 'und', "\n  <LineCode Error Systeme>\n   Error chars "+str(i+1+a[2])+": '"+ code[i+1+a[2]:i+1+a[2]+b[2]] + "'\n   Expected a numeral value in the second element of a substraction (-)\n   '" + b[0] + "' type value given"
        if a[0] == 'd' or b[0] == 'd': 
            return('d', a[1]-b[1], 1+a[2]+b[2])
        if a[0] == 'u' and b[0] == 'u': 
            return('u', abs(a[1]-b[1]), 1+a[2]+b[2])
        return('n', a[1]-b[1], 1+a[2]+b[2])
    
    if code[i] == '*':
        a = calc(i+1)
        assert a[0] in 'und', "\n  <LineCode Error Systeme>\n   Error chars "+str(i+1)+": '"+ code[i+1:i+1+a[2]] + "'\n   Expected a numeral value in the first element of a product (*)\n   '" + a[0] + "' type value given"
        b = calc(i+1+a[2])
        assert b[0] in 'und', "\n  <LineCode Error Systeme>\n   Error chars "+str(i+1+a[2])+": '"+ code[i+1+a[2]:i+1+a[2]+b[2]] + "'\n   Expected a numeral value in the second element of a product (*)\n   '" + b[0] + "' type value given"
        if a[0] == 'd' or b[0] == 'd': 
            return('d', a[1]*b[1], 1+a[2]+b[2])
        if a[0] == 'u' and b[0] == 'u': 
            return('u', a[1]*b[1], 1+a[2]+b[2])
        return('n', a[1]*b[1], 1+a[2]+b[2])
    
    if code[i] == '/':
        a = calc(i+1)
        assert a[0] in 'und', "\n  <LineCode Error Systeme>\n   Error chars "+str(i+1)+": '"+ code[i+1:i+1+a[2]] + "'\n   Expected a numeral value in the first element of a division (/)\n   '" + a[0] + "' type value given"
        b = calc(i+1+a[2])
        assert b[0] in 'und', "\n  <LineCode Error Systeme>\n   Error chars "+str(i+1+a[2])+": '"+ code[i+1+a[2]:i+1+a[2]+b[2]] + "'\n   Expected a numeral value in the second element of a division (/)\n   '" + b[0] + "' type value given"
        return('d', a[1]/b[1], 1+a[2]+b[2])

    if code[i] == '^':
        a = calc(i+1)
        assert a[0] in 'und', "\n  <LineCode Error Systeme>\n   Error chars "+str(i+1)+": '"+ code[i+1:i+1+a[2]] + "'\n   Expected a numeral value in the first element of a power (^)\n   '" + a[0] + "' type value given"
        b = calc(i+1+a[2])
        assert b[0] in 'und', "\n  <LineCode Error Systeme>\n   Error chars "+str(i+1+a[2])+": '"+ code[i+1+a[2]:i+1+a[2]+b[2]] + "'\n   Expected a numeral value in the second element of a power (^)\n   '" + b[0] + "' type value given"
        if b[1] >= 0 and b[0] in 'nu':
            if a[0] == 'd': 
                return('d', a[1]**b[1], 1+a[2]+b[2])
            if a[0] == 'u':
                return('u', a[1]**b[1], 1+a[2]+b[2])
            return('n', a[1]**b[1], 1+a[2]+b[2])
        return('d', float(a[1]**b[1]), 1+a[2]+b[2])
    
    if code[i] == '~':
        a = calc(i+1)
        assert a[0] in 'und', "\n  <LineCode Error Systeme>\n   Error chars "+str(i+1)+": '"+ code[i+1:i+1+a[2]] + "'\n   Expected a numeral value after the round operation (~)\n   '" + a[0] + "' type value given"
        return('n', round(a[1]), 1+a[2])
    
    if code[i] == '%':
        a = calc(i+1)
        assert a[0] in 'und', "\n  <LineCode Error Systeme>\n   Error chars "+str(i+1)+": '"+ code[i+1:i+1+a[2]] + "'\n   Expected a numeral value in the first element of a modulo (%)\n   '" + a[0] + "' type value given"
        b = calc(i+1+a[2])
        assert b[0] in 'und', "\n  <LineCode Error Systeme>\n   Error chars "+str(i+1+a[2])+": '"+ code[i+1+a[2]:i+1+a[2]+b[2]] + "'\n   Expected a numeral value in the second element of a modulo (%)\n   '" + b[0] + "' type value given"
        if a[0] == 'd' or b[0] == 'd': 
            return('d', a[1]%b[1], 1+a[2]+b[2])
        if a[0] == 'u' and b[0] == 'u': 
            return('u', a[1]%b[1], 1+a[2]+b[2])
        return('n', a[1]%b[1], 1+a[2]+b[2])
    
    if code[i] == '\\':
        a = calc(i+1)
        assert a[0] in 'und', "\n  <LineCode Error Systeme>\n   Error chars "+str(i+1)+": '"+ code[i+1:i+1+a[2]] + "'\n   Expected a numeral value after the square root operation (\\)\n   '" + a[0] + "' type value given"
        return('d', a[1]**0.5, 1+a[2])
    
    if code[i] == '=':
        a = calc(i+1)
        assert a[0] in 'un', "\n  <LineCode Error Systeme>\n   Error chars "+str(i+1)+": '"+ code[i+1:i+1+a[2]] + "'\n   Expected a integer value (u or n type) in the first element of an equality (=)\n   '" + a[0] + "' type value given"
        b = calc(i+1+a[2])
        assert b[0] in 'un', "\n  <LineCode Error Systeme>\n   Error chars "+str(i+1+a[2])+": '"+ code[i+1+a[2]:i+1+a[2]+b[2]] + "'\n   Expected a integer value (u or n type) in the second element of an equality (=)\n   '" + b[0] + "' type value given"
        return('n', int(a[1]==b[1]), 1+a[2]+b[2])
    
    if code[i] == '<':
        a = calc(i+1)
        assert a[0] in 'und', "\n  <LineCode Error Systeme>\n   Error chars "+str(i+1)+": '"+ code[i+1:i+1+a[2]] + "'\n   Expected a numeral value in the first element of a 'smaller than' operation (<)\n   '" + a[0] + "' type value given"
        b = calc(i+1+a[2])
        assert b[0] in 'und', "\n  <LineCode Error Systeme>\n   Error chars "+str(i+1+a[2])+": '"+ code[i+1+a[2]:i+1+a[2]+b[2]] + "'\n   Expected a numeral value in the second element of a 'smaller than' operation (<)\n   '" + b[0] + "' type value given"
        return('n', int(a[1]<b[1]), 1+a[2]+b[2])
    
    if code[i] == '>':
        a = calc(i+1)
        assert a[0] in 'und', "\n  <LineCode Error Systeme>\n   Error chars "+str(i+1)+": '"+ code[i+1:i+1+a[2]] + "'\n   Expected a numeral value in the first element of a 'bigger than' operation (>)\n   '" + a[0] + "' type value given"
        b = calc(i+1+a[2])
        assert b[0] in 'und', "\n  <LineCode Error Systeme>\n   Error chars "+str(i+1+a[2])+": '"+ code[i+1+a[2]:i+1+a[2]+b[2]] + "'\n   Expected a numeral value in the second element of a 'bigger than' operation (>)\n   '" + b[0] + "' type value given"
        return('n', int(a[1]>b[1]), 1+a[2]+b[2])
    
    if code[i] == '!':
        a = calc(i+1)
        assert a[0] in 'und', "\n  <LineCode Error Systeme>\n   Error chars "+str(i+1)+": '"+ code[i+1:i+1+a[2]] + "'\n   Expected a numeral value after the 'not' operation (!)\n   '" + a[0] + "' type value given"
        return('n', int(a[1]==0), 1+a[2])
    
    if code[i] == '&':
        a = calc(i+1)
        assert a[0] in 'und', "\n  <LineCode Error Systeme>\n   Error chars "+str(i+1)+": '"+ code[i+1:i+1+a[2]] + "'\n   Expected a numeral value in the first element of a 'and' operation (&)\n   '" + a[0] + "' type value given"
        b = calc(i+1+a[2])
        assert b[0] in 'und', "\n  <LineCode Error Systeme>\n   Error chars "+str(i+1+a[2])+": '"+ code[i+1+a[2]:i+1+a[2]+b[2]] + "'\n   Expected a numeral value in the second element of a 'and' operation (&)\n   '" + b[0] + "' type value given"
        return('n', int(a[1]*b[1]!=0), 1+a[2]+b[2])
    
    if code[i] == '|':
        a = calc(i+1)
        assert a[0] in 'und', "\n  <LineCode Error Systeme>\n   Error chars "+str(i+1)+": '"+ code[i+1:i+1+a[2]] + "'\n   Expected a numeral value in the first element of a 'or' operation (|)\n   '" + a[0] + "' type value given"
        b = calc(i+1+a[2])
        assert b[0] in 'und', "\n  <LineCode Error Systeme>\n   Error chars "+str(i+1+a[2])+": '"+ code[i+1+a[2]:i+1+a[2]+b[2]] + "'\n   Expected a numeral value in the second element of a 'or' operation (|)\n   '" + b[0] + "' type value given"
        return('n', int(a[1]+b[1]!=0), 1+a[2]+b[2])

    
    return ('$type', '$'+code[i], 0)


def set_type(type, value):
    if type in "un":
        return int(value)
    if type == 'd':
        return float(value)
    return value
    

def linecode(line):

    global code
    code = line + '$'

    assert len(code) > 1, "\n  <LineCode Error Systeme>\n   Error char 0\n   The LineCode is empty"


    assert not(' ' in code), "\n  <LineCode Error Systeme>\n   Error char "+ str(code.index(' ')) +": ' '\n   The LineCode can't have any space"

    global var_values
    global var_types
    global labels
    var_values = {}
    var_types = {}
    labels = {}


    i = 0
    k = 0


    while (i<len(code)-1):
        assert code[i] in "wrvscltg", "\n  <LineCode Error Systeme>\n   Error char "+str(i)+": '"+ code[i] + "'\n   Expected a function (in 'wrvsc')"

        if code[i] == 'w':
            k = get_number(i+1)
            i += 1+k[1]
            for j in range(k[0]):
                a = calc(i)
                print(a[1], end = '')
                i += a[2]

        if code[i] == 'r':
            try:
                var_values[code[i+1]] = set_type(var_types[code[i+1]],input(code[i+1]+': '))
            except:
                assert False, "\n  <LineCode Error Systeme>\n   Input Error\n   Expected '" + var_types[code[i+1]] + "' type input"
            i += 2

        if code[i] == 'v':
            var_types[code[i+1]] = code[i+2]
            i += 3

        if code[i] == 's':
            assert code[i+1] in var_types.keys(), "\n  <LineCode Error Systeme>\n   Error char "+str(i+1)+": '"+ code[i+1] + "'\n   Expected a known variable next the 'set' function (s)\n   Unknown variable " + code[i+1]
            a = calc(i+2)
            assert a[0] == var_types[code[i+1]], "\n  <LineCode Error Systeme>\n   Error chars "+str(i+2)+": '"+ code[i+2:i+2+a[2]] + "'\n   Expected a '" + var_types[code[i+1]] + "' type value to set the variable " + code[i+1] + "\n   '" + a[0] + "' type value given"
            var_values[code[i+1]] = set_type(var_types[code[i+1]],a[1])
            i += 2 + a[2]

        if code[i] == 'c':
            a = calc(i+1)
            assert a[0] == 'n', "\n  <LineCode Error Systeme>\n   Error chars "+str(i+1)+": '"+ code[i+1:i+1+a[2]] + "'\n   Expected a 'n' type value next the 'condition' function (c)\n   '" + a[0] + "' type value given"
            i += 1+a[2]
            assert code[i] != 'c', "\n  <LineCode Error Systeme>\n   Error char "+str(i)+": 'c'\n   conditionnal command (c) can't affect another conditionnal command (c <condition> c <condition> <command> it's impossible)"
            if not(a[1]):
                assert code[i] in "wrvsltg", "\n  <LineCode Error Systeme>\n   Error char "+str(i)+": '"+ code[i] + "'\n   Expected a function (in 'wrvsltg') after the condition function (c)"
                if code[i] == 'w':
                    k = get_number(i+1)
                    i += 1+k[1]
                    for j in range(k[0]):
                        a = calc(i)
                        i += a[2]
                elif code[i] == 'g':
                    i += 1
                elif code[i] == 'r':
                    i += 2
                elif code[i] == 'v':
                    i += 3
                elif code[i] == 's':
                    a = calc(i+2)
                    i += 2 + a[2]
                else: # l or t
                    a = calc(i+1)
                    i += 1 + a[2]
        
        if code[i] == 'l':
            a = calc(i+1)
            assert a[0] == 'n', "\n  <LineCode Error Systeme>\n   Error char "+str(i+1)+": '"+ code[i+1:i+1+a[2]] + "'\n   Expected a 'n' type value next the 'label' function (l)\n   '" + a[0] + "' type value given"
            i += 1+a[2]
            labels[a[1]] = i
        
        if code[i] == 't':
            a = calc(i+1)
            assert a[0] == 'n', "\n  <LineCode Error Systeme>\n   Error char "+str(i+1)+": '"+ code[i+1:i+1+a[2]] + "'\n   Expected a 'n' type value next the 'go to' function (t)\n   '" + a[0] + "' type value given"
            assert a[1] in labels, "\n  <LineCode Error Systeme>\n   Error char "+str(i)+": '"+ code[i:i+1+a[2]] + "'\n   The Label "+str(a[1])+" doesn't exist"
            i = labels[a[1]]


        
        if code[i] == 'g':
            novars = (len(var_types) == 0)
            nolabels = (len(labels) == 0)
            if novars and nolabels:
                print("┌───────────────────────┐")
                print("│ g Debug is empty      │")
                print("│  (no vars, no labels) │")
            if not(novars):
                print("┌─── Vars Type Value ───┐")
                for j in var_types.keys():
                    if j in var_values.keys():
                        print('│',j,var_types[j],var_values[j],(16-len(str(var_values[j])))*' ','│')
                    else:
                        print('│',j,var_types[j],"unset             │")
            if not(nolabels):
                if novars:
                    print("┌─── Labels Position ───┐")
                else:
                    print("├─── Labels Position ───┤")
                    for j in labels.keys():
                        print('│',j,labels[j],(20-len(str(j))-len(str(labels[j])))*' '+'│')
            print("└───────────────────────┘")
            i += 1


def linecodexe(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        file.close()
    if len(lines) == 1:
        code = lines[0]
    else:
        code = lines[0][:-1]
    linecode(code)
    

