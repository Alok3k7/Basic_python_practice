try:  # code that may raise an exception
    num = 0
    result = 10 / num
except ZeroDivisionError:     # code to handle the exception
    print("Error: Division by zero")
else:
    print("Result:", result)
finally:   # code that always runs
    print("process complete.")
