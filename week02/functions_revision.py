
# Function to find if a number a is divisible by b 
def is_divisible(a: int, b: int) -> bool: 
    return a % b == 0

# Function to convert fahrenheit (f) temperature to celsius and return it
def f2c(f: float) -> float:
    return (f - 32) * 5 / 9
    

# print(is_divisible(10, 3))
print(f2c(100.0))