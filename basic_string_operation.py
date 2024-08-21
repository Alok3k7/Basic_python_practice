# 1. Creating Strings
my_string = "Hello, World!"  # Enclose text in single (' '), double (" "), or triple (''' ''' or """ """) quotes.
print(my_string)
# 2. String Concatenation
str1 = "Hello"
str2 = "All Teammate!"
ans = str1 + "," + str2  # Join strings using the` + `operator.
print(ans)
# 3.Finding String Length
length_string = "We Are Here to Learn ."
length = len(length_string)  # Use the len() function to determine the length of a string.
print(length)
# 4.String Indexing and Slicing
index_slice_string = "Python is very powerful language "
char = index_slice_string[0]  # Access individual characters or slices of a string using square brackets [ ]
print(char)
substring = index_slice_string[6:24]
print(substring)
# 5. String Methods
my1_string = " Alok at Tricera and some her Personal learning   "
uppercase = my1_string.upper()
print(uppercase)
lowercase = my1_string.lower()
print(lowercase)
stripped = my1_string.strip()
print(stripped)
replaced = my1_string.replace("Alok", "Yogesh")
print(replaced)
words = my1_string.split(",")  # Splits the string into a list using comma as the delimiter
print(words)
"""6.String Formatting  method also we use at string formatting"""
# 7.String Search and Manipulation
search_manipulation = "Hello, Tricera!"
contains_hello = "Hello" in search_manipulation
print(contains_hello)  # Check for substring existence with in keyword and find positions with find() or index()methods.
position = search_manipulation.find("Tricera")
print(position)
# 8. String Escaping
escaped_string = "This is a \"quoted\" string."  # Use escape sequences to include special characters within a string.
print(escaped_string)
# 9.String Concatenation with Variables
name = "Alok"
greeting = "Hello, " + name + "!"
formatted_greeting = "Hello, {}!".format(name)
print(greeting)
