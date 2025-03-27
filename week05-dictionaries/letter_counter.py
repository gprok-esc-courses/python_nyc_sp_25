
letters = {}

sentence = input("Sentence: ")

sentence = sentence.lower()

for ch in sentence:
    if ch in letters:
        letters[ch] += 1
    else:
        letters[ch] = 1

for key in letters:
    print(key, letters[key])