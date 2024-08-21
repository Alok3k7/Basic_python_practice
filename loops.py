# Loops
# 1. for loop
my_list = [1, 2, 3, 4, 5, 6, "apple", "banana", "cherry"]
for my_index in my_list[3:-1]:  # Here my_index is variable that store the value of index by list
    print(my_index)

# 2. While Loop
# Here we print the table of 2
table = 0
while table < 22:  # Here while loop will start when condition less than 22 that will stop.
    print(table)
    table += 2
# 3.
# break: Terminates the loop prematurely, even if the loop condition is still True.
# continue: Skips the current iteration of the loop and continues with the next iteration.
# the use of these control statements:


for index in range(10):
    if index == 6:
        continue  # Skip iteration when i is 3
    if index == 9:
        break  # Terminate the loop when i is 7
    print(index)

# loops are done
