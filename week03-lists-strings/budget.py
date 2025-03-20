

print("Supermarket Budget")

budget = float(input("What is your budget? "))
total = 0
prices = []

while total <= budget:
    print("Total:", total)
    price = float(input("Add item's price: "))
    prices.append(price)
    total += price 

print("Total:", total)
print("You exeeded the budget")

print("Items' price:", end=' ')
for p in prices:
    print(p, end=' ')
print()

response = input("Do you want to remove max value? ")
if response == 'y':
    max_price = max(prices)
    total -= max_price 
    prices.remove(max_price)
    print("Max price", max_price, "removed. Total:", total)
