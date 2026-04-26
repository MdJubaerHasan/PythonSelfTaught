
"""
Lists in python is an ordered, mutable (changeable) collection that can hold a mix of data types
"""

my_list = [1, "Two", 3.14, True]

# Check ID now and again Later
print(f"my_list ID : {id(my_list)}")

"""

Python lists are zero-indexed
Using negative index returns from the rare of the list 
"""

print(my_list[0])
print(my_list[-1])


"""
List slicing: Access a range of items using list[start:stop:step]

In the above expression, start value is inclusive, stop value is exclusive
Ex: my_list [0:3:1] will return [1, "Two", 3.14]

"""

print(my_list[0:3:1])

"""
As mentioned, strings are Mutable, meaning they can be changed in place 
"""

# Adding items

your_list = [5, 5, 6, "Seven", 8]

my_list.append(4) # adds the element at the end of the list
my_list.insert(0, 0) # inserts a value at a specific position
my_list.extend(your_list)
print(my_list)

# To prove that it is the same object
print(f"my_list ID : {id(my_list)}")


# Removing items
print(f"my_list : {my_list}")
my_list.pop(0) # This will remove and return the first item
print(my_list)
my_list.pop() # This will remove and return the last item by default
print(my_list)
my_list.remove(5) # This will remove the first occurrence of a value, else it will throw an error if item missing
print(my_list)
del my_list[-1] # Will delete it by index
print(my_list)


"""
List Comprehension: Concise way of creating lists
"""

# Creating a list of squares of even numbers 1 to 20:
squares = [x**2 for x in range(1,21) if x%2 == 0]
print(squares)

"""
List.sort() sorts the List in places 

sorted(list) -> Returns a new sorted list and the original remains same
"""
unsorted_list = [6, 3, 7, 8 , 10]
print(sorted(unsorted_list))
print(sorted(unsorted_list, reverse=True)) # Reverse sorted
print(unsorted_list)

"""
Some searching method in a list :
value in list -> returns true if value exits 
list.index(value) -> returns the index of the first occurrence
list.count(value) -> returns how many times a value appears 
"""

elements = ["H2O", "CO2", "COOH", "Ni", "H2O", "CO2"]

print("H2O" in elements)
print(elements.index("CO2"))
print(elements.count("H2O"))


"""
Copying list items:

As variables are just labels, doing something like list_a = list_b will not create a new list
list_a = list_b.copy() will create a new list of same elements of list_b
Alternative: list_a = list_b[:]
"""
list_a = ["a", "a", "a", "a", "a"]
list_b = list_a.copy()
print(f"list_a = {list_a}")
print(f"list_b = {list_b}")

# Let's update the list_b and check

list_b[0] = "b"
list_b[-1] = "b"

print(f"After update, list_a = {list_a}")
print(f"After update, list_b = {list_b}")


"""
For a complex nested list , we have to use DeepCopy() otherwise the inner lists element will be same for both lists
"""

complex_list_a = [[23, 24], [29, 30], 31, 32]
complex_list_b = complex_list_a[:]
print(f"Before update: CLA -> {complex_list_a}")
print(f"Before update: CLB -> {complex_list_b}")

complex_list_a[0][1] = 25
complex_list_a[2] = 61

print(f"After update: CLA -> {complex_list_a}")
print(f"After update: CLB -> {complex_list_b}")

"""
it is visible that despite being separate lists , value in the index [0][1] changed for both
"""
from copy import deepcopy
complex_list_c = deepcopy(complex_list_a)

print(f"Before update: CLA -> {complex_list_a}")
print(f"Before update: CLC -> {complex_list_c}")

complex_list_a[0][1] = 0
complex_list_a[2] = 0

print(f"After update: CLA -> {complex_list_a}")
print(f"After update: CLC -> {complex_list_c}")



"""
BigO Complexity:

appending -> O(1)
pop(last item) -> O(1)
Insert/delete (start/middle) -> O(n)
Search -> O(n)
"""

"""
###
Never remove items from a list while iterating through , it skips indices 
Solution: iterate over a copy for item in my_list[:]
Clarity ---> my_list[:] creates a shallow copy of the list 
Never use an empty list as a default argument in a function call
as it will be a single persistent list for all calls
Solution : use None
###
"""