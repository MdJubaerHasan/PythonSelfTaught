"""
In python, variables are not containers that hold values
A python variable is a LABEL/TAG attached to an object in the memory
"""

# An example would be clear using id()
x = 1
print(id(x))

x = 5
print(id(x))

"""
This shows these variables are not containers. 

Python variables are dynamic types, can switch between any data type

"""

x = "String!"
print(x)

"""
Data Types:

int -> Integer -> ex: 69, -23 -> Whole numbers of arbitrary precision.
float - > Floating point -> 2.0, 3.45 -> Decimal Numbers (IEEE 754 double precision)
str -> String -> "Python" -> Sequence of Unicode Characters
bool -> Boolean -> True, False -> Truth Values
NoneType -> None -> None -> Represents the absance of a value 


"""

x = 69
y = 2.0
z = "Numbers"
truth = True
false = False
no_value = None


"""
Mutability: determines whether an object can be modified after it is created.

Immutable: changing an immutable object will create a new object in memory and move the label to it.

Immutable objects type:
int, float , str, tuple, bool, frozenset 

Ex: a = 5 and a = a + 1 is not the same object

Mutable types:
list, dict, set, bytearray

Appending or removing items from these does not create a new object type.

list_a = [1, 2] and list_a = [1, 2, 3] is same list object

"""

"""
Aliasing: Multiple variables pointing to the same memory ID.
"""

var_a = 6
var_b = var_a


print(id(var_b))
print(id(var_a))
