# Index

test_str = "Welcome to Python"
print("Test string:,", test_str)
print("First string:", test_str[0])
print("Second string last character Index1:", test_str[-1])


# Length of string
liststring = len(test_str)
print("Total Length given string:",liststring)


# All String print using loop
# for item in range(len(test_str));
#     print(f"Item {item}:", {test_str[item]})
for(index, character) in enumerate(test_str):
    print(index, character)
# String slicing
print("Character of index 0 to 5:",test_str[0:5])
print("Character of index last character:",test_str[16])
