
countries = {}
file = open('files/uefa.csv', encoding="utf-8")

lines = file.readlines()

for line in lines[1:]:
    parts = line.split(',')
    country = parts[13]
    if country in countries:
        countries[country] += 1
    else:
        countries[country] = 1

for key in countries:
    print(key, countries[key])