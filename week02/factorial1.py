

def factorial(n: int) -> int:
    """
    Calculates and returns the factorial of a positive integer n
    """
    f = 1

    for i in range(1, n+1):
        f = f * i

    return f

try:
    n = int(input("Give n: "))

    if n < 0:
        print("Positive numbers only")
    else:
        f = factorial(n)

        print("Factorial: ", f)
except ValueError as ve:
    print("n must be a number")

