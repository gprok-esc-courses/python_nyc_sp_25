
data = open('files/students.csv')

lines = data.readlines()

for line in lines:
    parts = line.strip().split(',')
    parts[2] = float(parts[2])
    print(parts)