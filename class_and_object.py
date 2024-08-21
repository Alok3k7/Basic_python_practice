# Define a class called 'humans'
class baby:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def baby(self):
        print(f"Name: {self.name}, gender: {self.gender},Age: {self.age}")


# Create instances (objects) of the 'humans' class
humansbaby1 = baby("Pratham nath Tiwari",  "Male", 8)
humansbaby2 = baby("Reesha Tiwari",  "female", 4)

# Display information about the humans
print("baby 1:")
humansbaby1.baby()
print("\n baby 2:")
humansbaby2.baby()
