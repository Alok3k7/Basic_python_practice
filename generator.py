def fibonacci_generator():
    a, b = 0, 1
    while True:   # checking the condition
        yield a  # using this number print in sequence wise
        a, b = b, a + b


fib = fibonacci_generator()

for _ in range(10):  # Print the first 10 Fibonacci numbers

    print(next(fib))
