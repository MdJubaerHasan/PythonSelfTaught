# An ordered collection of items
# A list is an ordered, mutable (changeable) collection that allows duplicate members.
# Python uses zero-based indexing. The first item is [0]
# Negative Indexing: -1 refers to the last item.
# Lists are Generally used for Homogenious data
class Cat:
    def __init__(self, name):
        self.name = name

cat = Cat("Mew")


list1 = ["New", "1", "Abc", cat.name, cat.name, "pew"]

print(list1)
print(list1[2])

item = list1[-2]
if isinstance(item, Cat):
    print(item.name)

# Intermediate: Slicing & Methods
# Slicing: Access a range of items using list[start:stop:step].

print(list1[0: -1: 2])


# Common Methods:
#
# .append(x): Adds x to the end.
list1.append("Mara")

# .insert(i, x): Inserts x at position i.
list1.insert(0, "Babu")

# .pop(): Removes and returns the last item.
list1.pop()

# .sort(): Sorts the list in place.
list1.sort()
print(list1)

# List Comprehensions
# [expression for item in iterable if condition]

squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares)

# Advanced Memory & Copying

# aliasing

list_a = ["a"]
list_b = list_a
list_b.append("b")

print(list_a)

# variables are like labels and one variable can have multiple labels


# Shallow Copy: Creating a backup

# The container (the list) is new.
# The contents (the objects inside) are still just references to the original items.

list_c = list_a.copy() # copy method
list_d = list_a[:] # full slice

list_a.append("c")

list_c.append("d")

print(f"list_c:  {list_c}")
print(f"list_d:  {list_d}")
print(f"list_b:  {list_b}")
print(f"list_a:  {list_a}")

list_a.append(cat)
print(f"list_a:  {list_a}")
list_e = list_a.copy()
print(f"list_e:  {list_e}")
list_e[-1].name ="Garfield"
print(f"list_a cat name {list_a[-1].name}")
print(f"list_e cat name {list_e[-1].name}")


# Deep Copy
# creates a copy where the objects inside are also brand-new duplicates
# This essentially "recursively" copies everything it finds

import copy

list_f = copy.deepcopy(list_a)
list_f[-1].name = "Tony"

print(f"list_a cat name {list_a[-1].name}")
print(f"list_f cat name {list_f[-1].name}")