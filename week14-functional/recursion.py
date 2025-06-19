# Display values from n down to 0
def display(n):
    if n >= 0:
        print(n)
        display(n - 1)


display(5)


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return factorial(n - 1) * n
    

print(factorial(5))


def fibonacci(n):
    if n == 0 or n == 1:
        return n 
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    

print(fibonacci(4))