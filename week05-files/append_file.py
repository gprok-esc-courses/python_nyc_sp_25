
file = open('files/out.txt', 'a')

fname = input("First Name: ")
lname = input("Last Name: ")

file.write(fname + " " + lname + "\n")