# Most of the basic data types you use daily in Python are immutable:

# Numbers: int, float, complex
#
# Strings: str
#
# Tuples: tuple
#
# Frozen Sets: frozenset
#
# Bytes: bytes


x = 10
print(id(x))
x = 11
print(id(x))

# Tuple

# A tuple is an ordered, immutable collection of elements. Once you define it,
# you cannot add, remove, or change its items. In Python,
# tuples are defined by placing elements inside parentheses ()
# they can be used as keys in a dictionary as they are hashable
# Tuples are Generally used for Heterogeious data
# Fixed block data structure hence faster to iterate, memory-efficient 
co_ordinates = (58,29,40,40,0,30)
print(co_ordinates[-1])
# co_ordinates[2] = 10 will throw error as its immutable
my_info = ("Octane", 28, "Apex Legends")
single_elem = (9,)
nested_tuples = ((1,2), (3,4), (5, 6))
#
# # Unpacking
x, y, z = nested_tuples
print(f"x : {x}, y: {y}, z: {z}")

users = [("alice", 31) , ("bob" , 29), ("billy", 28)]

for name, age in users:
    print(f"name: {name} is {age} years old")

swap_a = 0
swap_b = 100

print(f"before swap_a:  {id(swap_a)}")
print(f"before swap_b:  {id(swap_b)}")

swap_a, swap_b = swap_b, swap_a

print(f"after swap_a:  {id(swap_a)}")
print(f"after swap_b:  {id(swap_b)}")

results = ["Gold", "Silver", "Bronze", "Fourth", "Fifth"]

first, second, third, *others = results
print(first)