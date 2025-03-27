import csv 

file = open('files/uefa.csv', encoding='utf-8')

reader = csv.DictReader(file)

for row in reader:
    print(row)