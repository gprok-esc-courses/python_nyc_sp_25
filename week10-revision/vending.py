import random

amount = random.random() * random.randint(1, 100)
amount = round(amount, 1)

print(amount)

payment = float(input("Pay: "))

diff = payment - amount
diff = round(diff, 1)
print(diff)

change_values = [2, 1, 0.5, 0.2, 0.1]
# Calculate the change

# 2 euros
print("====> 2 euros")
result = int(diff) // 2
print(result)

diff = diff - (result * 2)
diff = round(diff, 1)
print(diff)
# 1 euros
print("====> 1 euros")
result = int(diff) // 1
print(result)

diff = diff - (result * 1)
diff = round(diff, 1)
print(diff)
# 0.5 euros
print("====> 0.5 euros")
result = diff  / 0.5
print(int(result))

diff = diff - (int(result) * 0.5)
diff = round(diff, 1)
print(diff)
# 0.2 euros
print("====> 0.2 euros")
result = diff  / 0.2
print(int(result))

diff = diff - (int(result) * 0.2)
diff = round(diff, 1)
print(diff)
# 0.1 euros
print("====> 0.1 euros")
result = diff  / 0.1
print(int(result))
