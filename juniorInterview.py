# [expression for item in iterable if condition]
# for even squares of 1 to 20
# in range, (start is inclusive, but end) is exclusive
#
squares = [x**2 for x in range(1,21) if x%2 == 0]

# print(squares)

# Never use mutable objects (like lists, dictionaries, or sets) as default arguments
# unless you intentionally want all function calls to share the exact same object.
# Example:
# def add_item(item, item_list=[]):
#     item_list.append(item)
#     return item_list
#
# list1 = add_item("apple")
# list2 = add_item("banana")
# In Python, default arguments are evaluated only once,
# at the exact moment the function is defined, not every time the function is called.

def add_item(item, item_list=None):
    if item_list is None:
        item_list = []
    item_list.append(item)
    return item_list

list1 = add_item("apple")
list2 = add_item("banana")
print(list2)