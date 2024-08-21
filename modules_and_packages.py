# we have one  files  that name my project then we store two function first one that store math_operations and
# the  second one string_operations.py
# math_operations.py 
import math
import this 

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed."
    return x / y


# string_operations.py

def capitalize(text):
    return text.capitalize()


def reverse(text):
    return text[::-1]


def count_words(text):
    words = text.split()
    return len(words)


# then we use__init__ file that initialization priority file my project  read as a package

# we put the files on that file__init__

# main.py moduels and packages


"""from my_project import math_operations, string_operations"""

# Math operations
result_add = math_operations.add(512, 3)
result_divide = math_operations.divide(10, 2)
result_sub = math_operations.subtract(10, 7)

print("Addition Result:", result_add)
print("Division Result:", result_divide)
print("Subtract Result:", result_sub)

# String operations
text = "hello, tricera alok is here"
capitalized_text = string_operations.capitalize(text)
reversed_text = string_operations.reverse(text)
word_count = string_operations.count_words(text)

print("Capitalized Text:", capitalized_text)
print("Reversed Text:", reversed_text)
print("Word Count:", word_count)
