import json

# 1. Structure the data using Python lists and dictionaries
employees = [
    {"id": 101, "name": "Alice", "department": "Engineering", "active": True},
    {"id": 102, "name": "Bob", "department": "Sales", "active": False},
    {"id": 103, "name": "Charlie", "department": "Design", "active": True}
]

# 2. Write the data to a file
with open("employees.json", "w") as file:
    # dump takes the data first, then the file object to write into
    # indent=4 tells Python to format it vertically with 4 spaces per level
    json.dump(employees, file, indent=4)

complex_data = [
    # Element 0: A dictionary representing a user profile
    {
        "user_id": 1042,
        "username": "coder_jane",
        "active": True,
        # A list nested inside the dictionary
        "roles": ["admin", "editor", "viewer"],
        # A tuple nested inside the dictionary (e.g., unchanging coordinates)
        "last_login_location": ("New York", 40.7128, -74.0060),
        # A dictionary nested inside the dictionary
        "preferences": {
            "theme": "dark",
            "notifications": True
        }
    },

    # Element 1: Another dictionary, showcasing lists inside lists
    {
        "user_id": 1043,
        "username": "data_dan",
        "active": False,
        # A nested list inside another list
        "roles": ["viewer", ["guest_access", "read_only"]],
        "last_login_location": ("London", 51.5074, -0.1278),
        "preferences": {
            "theme": "light",
            "notifications": False
        }
    },

    # Element 2: A tuple sitting directly in the main list,
    # containing a string and a dictionary
    ("metadata", {"generated_on": "2026-04-21", "system_version": "3.1.4"})
]

with open('user_data.json', 'w') as json_file:
    # json.dump writes the Python object directly to the file object
    # indent=4 provides the clean, human-readable formatting
    json.dump(complex_data, json_file, indent=4)