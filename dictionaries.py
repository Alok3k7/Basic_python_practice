# Creating a dictionary to store information about a person
alok_at_tricera = {
    "name": "Aloknath Tiwari",
    "age": 20,
    "city": "Pune",
    "email": "alokattriceratech@bbbb"
}

# Accessing values
print("Name:", alok_at_tricera["name"])
print("Age:", alok_at_tricera.get("age"))

# Modifying values
alok_at_tricera["age"] = 31
print("Updated Age:", alok_at_tricera["age"])

# Adding a new key-value pair
alok_at_tricera["country"] = "BHARAT"
print("Country:", alok_at_tricera["country"])

# Removing a key-value pair
del alok_at_tricera["email"]
print("Dictionary after removing 'email':", alok_at_tricera)

# Checking if a key exists
if "city" in alok_at_tricera:
    print("City is present in the dictionary")

# Iterating over the dictionary
print("Iterating over the dictionary:")
for key, value in alok_at_tricera.items():
    print(key + ":", value)
