
file = open('files/lipsum.txt')

lines = file.readlines()

for line in lines:
    print(line)