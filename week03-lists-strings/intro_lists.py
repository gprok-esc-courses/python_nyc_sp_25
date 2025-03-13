
data = [34, 23, 45, 87, 44, 21, 90]

print(data[0])
print(len(data))

for i in range(len(data)):
    print(i, data[i])

for value in data:
    print(value)

# Calculate the average of values in data
total = 0
for value in data:
    total = total + value 

print("Average:", total / len(data))

# Find the minimum in the list
minimum = data[0]
for value in data:
    if value < minimum:
        minimum = value

print("MIN:", minimum)
print(min(data))

# Last element in the list
print(data[len(data)-1])
print(data[-1])

data.append(108)
print(data[-1])

data.pop(0)
print(data[0])