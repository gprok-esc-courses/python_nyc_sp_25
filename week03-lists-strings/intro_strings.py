
s = "This is a string"

print(len(s))
print(s[0])
print(s[-1])

letter = input("Give a letter: ")
counter = 0
for ch in s.lower():
    if letter == ch:
        counter += 1

print(letter, "found", counter, "times")

s2 = "     another string with head and trailing spaces        "
print(len(s2))
s2 = s2.strip()
print(len(s2))

words = s2.split()
print(words)
print(len(words))

# Ask user for a letter and find and print the words 
# that start with this letter

letter = input("Give a letter: ")
for word in words:
    if word[0] == letter:
        print(word)

# Find the longest word in the list
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print("Longest word:", longest)

