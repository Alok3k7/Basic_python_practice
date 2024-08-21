# decorator
def my_decorator(func):  # first we create a function that called decorator.
    def wrapper():  # then wrapper the statement .
        print("before execution of the function")
        func()  # then we drop an empty function on it
        print("after execution of the function")

    return wrapper  # then we return the function


@my_decorator  # then we call @decorator fulfill that empty function.
def greet():
    print("alok is there")  # we call function.


greet()
