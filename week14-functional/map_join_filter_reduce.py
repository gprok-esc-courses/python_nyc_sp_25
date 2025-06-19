from functools import reduce

def increase(x):
    return x + 1

def add_data(a, b, c):
    return a + b + c

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

increased_data = map(increase, data)
print(data)
print(list(increased_data))

matrix_sum = map(add_data, [1, 2, 3], [4, 5, 6], [7, 8, 9])
print(list(matrix_sum))

cities = ['Athens', 'London', 'New York', 'Paris', 'Amsterdam']

def name_len(n):
    return len(n)

cities_len = map(lambda n: len(n), cities)
print(list(cities_len))

cities_str = ", ".join(cities)
print(cities_str)


even_nums = filter(lambda n: n % 2 == 0, data)
print(list(even_nums))

even_nums_2 = []
for n in data:
    if n % 2 == 0:
        even_nums_2.append(n)


total = reduce(lambda a, b: a + b, data)
print(total)
