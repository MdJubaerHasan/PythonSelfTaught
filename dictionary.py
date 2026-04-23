# A collection of "Key-Value" pairs.
# A dictionary is an unordered (technically ordered as of Python 3.7+), mutable collection of key-value pairs.
# access values via their keys, not indices
key_values = {"User" : "Admin",
              "password" : "tungu nungu",
              1: 2}

print(key_values["password"])

# Intermediate: Dictionary Methods
# .get(key, default): Safely access a key without crashing if it doesn't exist.
print(key_values.get(1))
print(key_values.get(2))

# .keys() / .values() / .items(): Return views of the keys, values, or both.

print(key_values.keys())
print(key_values.values())
print(key_values.items())

# .update({key: value}): Merges another dictionary or updates existing keys.

key_values.update({"User" : "Guttu"})
print(key_values.items())


