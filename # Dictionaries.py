# Dictionaries (key-value pairs)
person = {
    "name": "Bob",
    "age": 25,
    "city": "New York"
}
print("Person Dictionary:", person)

# Accessing dictionary values
print("Person's Name:", person["name"])

# Looping through a dictionary
print("Person Details:")
for key, value in person.items():
    print(key + ":", value)