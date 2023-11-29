# THE FUNCTIONS

- `w`: write (output values)
- `r`: read  (input a value)
- `v`: var   (initialize variables)
- `s`: set   (set the value of a variable)
- `c`: cond  (equivalent of a "if")
- `l`: label (store the position)
- `t`: go to (go to a Label)

+ `g`: debug command

## THE WRITE FUNCTION (w)

The write function can write several values to the user.

The fisrt argument of the write function is a raw number. This number indicate the number of values printed.

> Example: `w3n12ssc!` print "12 !" (who have three elements: the number 12 (n12), the special character space (ss) and the chararcter "!" (c!))

All types are writable

(the "Hello World!" code can be `w13cHceclclcosscWcocrclcdc!sl`)

## THE READ FUNCTION (r)

The read function can ask to the user the value of a variable

The read function expects just one argument: the variable name

> Example: rk ask to the user a value with "k: " and store it in the variable k

## THE VAR FUNCTION (v)

The var function is used to initialize variables. This function is required to use a variable.

The var function expects two arguments: the name of the new variable and its type.

> Example: vkn create a new variable named 'k' and its type is 'number' (n)

The types:

- n - integer number
- u - unsigned integer number
- d - decimal number
- c - character
- t - type (yes, type is a type)

The variables names:

- The variables names must just one character but any chararcter without space and linebreak
- (can be a A 5 \ + . $ µ...)

## THE SET FUNCTION (s)

The set function can set the value of a variable. The function must be initialized with the var function (v) before be set by the set function (s).

The set function expects two argument: the name of the variable, nad the new value
 -> Example: skn12 set the variable 'k' at 12

The type of the value and the type of the variable must the sames.

## THE COND FUNCTION (c)

The cond function is an equivalent of the "if" function.
It run the next function only if the condition is true.

The cond function expected two arguments: the condition and the command.
 -> Example: c=vkn12w3cscacy run the function 'w3cscacy' if the variable k is equal to 12

/!\ The function powered by a cond can't be an cond function
 ( c `<condition1>` c `<condition2>` `<function>` is impossible, you must write c `<condition1>` & `<condition2>` `<function>`)

# VALUES

When a function or an operation expects a "value", it expects a raw value (as a number, a character...) or an operation (an addition, a product...)

The raw values start with a prefix (n12 for 12) and the operation strat with the operation (+n12n12 for 12+12)

## RAW VALUES

n: natural number  (type n)
z: negative number (type n)
u: unsigned number (type u)
d: decimal number  (type d)
v: variable        (type of the variable)
c: character       (type c)
s: special char    (type c)

## NATURAL NUMBERS (n)

The natural number prefix is juste used for the positive number
 -> Example: n12 for the number 12

The type of "n12" is a signed integer number (n)

You can't right "n-12", for this use the prefix z

## NEGATIVE NUMBERS (z)

The negative number prefix introduce a negative number
 -> Example: z12 for the number -12

The type of "z12" is a signed integer number (n)

## UNSIGNED NUMBERS (u)

The unsigned number prefix introduce a unsigned number
 -> Example: u12 for the number 12

The type of "u12" is a unsigned integer number (u)

## DECIMAL NUMBERS (d)

The decimal number prefix is followed by the integer part, the lettre n or z to indicate the symbol of the number and the decimal part.
 -> Examples: d12n7 for the number 12.7
              d12z7 for the number -12.7

The type of "d12n7" or "d12z7" is a signed decimal number (d)

## VARIABLE (v)

The variable prefix v is used to get the value of a variable in a function
 -> Example: vk to get the value of the variable k

The type of "vk" depending on the type of the variable k

## CHARACTER (c)

The simple character prefix c is used to get all the character without space and linebreak
 -> Example ce to get the character "e"

The type of "ce" is a chararcter (c)

## SPECIAL CHARACTER (s)

The special character prefix s is used to get the characters space (with s) and linebreak (with l)
 -> Examples: ss to get the character space
              sl to get the character linebreak

The type of "ss" or "sl" is a chararcter (c)

# OPERATIONS

The operations expects one or two arguments placed AFTER the operation symbol
 -> Example: +n12n13 for 12+13

List of the operations expecting two arguments:

+ Addition

- Sustraction

* Product
  / division
  ^ power
  % modulo
  = equality
  < smaller than

> bigger than
> & boolean and
> | boolean or

List of the operations expecting only one argument:
_ Inverse     (same as *(-1) )
~ Round
\ Square Root
! Boolean not
t Type        (return the type of the argument)
