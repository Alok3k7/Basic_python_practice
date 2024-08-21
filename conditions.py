# conditions
# if , elif , else.
age = 22

if age < 18:  # The if statement is used to execute a block of code if a specified condition is true.
    print("You are a minor.")
elif 18 <= age < 65:  # The elif statement is used to check additional conditions if the preceding if or eli
    # conditions are false. You can have multiple elif blocks
    print("You are an adult.")
else:  # The else statement is used to define a block of code that is executed if none of the preceding conditions
    print("You are a senior citizen.")
# 2.Logical operators
condition1 = True
condition2 = False
result_and = condition1 and condition2  # logical AND: and
print(result_and)
result_or = condition1 or condition2  # Logical OR: or
print(result_or)
# 3.Comparison operators
a = 45
b = 22
is_equal = a == b  # Equal to: ==
print(is_equal)
is_not_equal = a != b  # Not equal to: !=
print(is_not_equal)
is_greater = a > b  # Greater than: >
print(is_greater)
is_less = a < b  # Less than: <
print(is_less)
