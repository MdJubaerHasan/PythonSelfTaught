# 'r': Read (default). Errors if the file doesn't exist.
# 'w': Write. Creates a new file or overwrites an existing one.
# 'a': Append. Adds new data to the end of the file.

# with open("sometext.txt", "w") as file:
#     file.write("Tonga Bonga")
#
# with open("sometext.txt", "r") as file:
#     content = file.read()
#     print(content)
#
# with open("sometext.txt", "a") as file:
#     file.write("\nUnga Bunga Nunga\n")
#
#
# with open("sometext.txt", "r") as file:
#     content = file.read()
#     print(content)


with open("massive_text.txt", "r") as file:
    for line in file:
        # Process one line at a time
        print(line.strip())