# 1.String Concatenation:
name = "Alok"
age = 20
message = "My name is " + name + " and I am " + str(age) + " years old."
print(message)
# 2 .String Interpolation with f-strings
name = "Aditya"
age = 18
message = f"My name is {name} and I am {age} years old."
print(message)
# 3 .String Formatting with the str.format() method
teammate_1 = "Harshal"
teammate_1_age = 21
message = "My name is {} and I am {} years old.".format(teammate_1, teammate_1_age)
print(message)
# 4. String Formatting with %-formatting
teammate_2 = "yogesh"
teammate_2_age = 22
message = "My name is %s and I am %d years old." % (teammate_2, teammate_2_age)
print(message)
# 5. String Formatting using str.join()
names = ["Alok", "harshal", "yogesh"]
joined_names = ", ".join(names)
print(f"Our team members are: {joined_names}")
# 6. String Formatting with Template Strings 
from string import Template

brother_name = "gauraw"
brother_age = 24
template = Template("My  brother name is $name and He was $age years old.")
message = template.substitute(name=brother_name, age=brother_age)
print(message)

