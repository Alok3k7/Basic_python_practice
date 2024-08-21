# Here's how you can create and work with lists in Python:

# 1. **Creating Lists**:You can create a list by enclosing a comma-separated sequence of values in square brackets:
the_list = [1, 2, 3, 4, 5]

# Lists can contain elements of different data types:


mixed_list = [1, "apple", True, 3.14]

# 2. **Accessing Elements**:You can access elements of a list using indexing. Indexing starts at 0 for the first
# element:

print(the_list[0])  # Output: 1
print(the_list[2])  # Output: 3

# You can also use negative indexing to access elements from the end of the list:

print(the_list[-1])  # Output: 5 (last element)

# 3. **Modifying Lists**: Lists are mutable, so you can change their contents:

# Adding elements:
the_list.append(6)  # Adds 6 to the end of the list
the_list.insert(2, 7)  # Inserts 7 at index 2

# Removing elements:


the_list.remove(3)  # Removes the first occurrence of 3
popped_element = the_list.pop(4)  # Removes and returns the element at index 4

# Updating elements:
the_list[1] = "banana"  # Updates the element at index 1

# 4. **Slicing**:You can create slices of a list to access multiple elements at once:
print(the_list[1:3])  # Output: [2, 3]

# 5. **Length of a List**:You can find the number of elements in a list using the `len()` function:

length = len(the_list)  # length will be 5

# 6. **Iterating Over a List**: You can use a `for` loop to iterate over the elements of a list:


for item in the_list:
    print(item)
