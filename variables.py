# Variables and type
# In Python, a variable is a symbolic name or identifier that is used to store and reference data
# values. Think of a variable as a container that can hold different types of information, such as numbers, text,
# or complex data structures. Variables are fundamental to programming because they allow you to manipulate and work
# with data in your programs

# 1. **Integers (int)**: Used to store whole numbers.
a = 10  # a is variable
print(a)
# 2.**Floating-Point Numbers (float)**: Used to store decimal numbers.
floating = 3.14
print(floating)
# 3. **Strings (str)**: Used to store text or characters.
char = "Alice"
print(char)
# 4. **Boolean (bool)**: Used to store either `True` or `False` values, often used in conditional statements.
boolean = True
print(boolean)
# 5. **Lists**: Used to store an ordered collection of items, which can be of different data types.
the_list = [1, 2, 3, "apple"]
print(the_list)
# 6. **Tuples**: Similar to lists but immutable (cannot be changed after creation).
my_tuple = (1, 2, 3, "banana")
print(my_tuple)
# 7. **Dictionaries (dict)**: Used to store key-value pairs.
dic = {"name": "Alice", "age": 30}
print(dic)
# 8. **Sets**: Used to store unique and unordered collections of items.
my_set = {1, 2, 3, 3, 4}
print(my_set)  # Contains only unique values
# 9. **NoneType (None)**: Used to represent the absence of a value or a null value.
result = None
print(result)


# 10. **Custom Objects (Classes)**: You can define your own data types by creating classes.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("Alice", 30)
print(person.name)
print(person.age)
