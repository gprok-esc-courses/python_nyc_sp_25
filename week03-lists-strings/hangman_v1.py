import random

words = ['object', 'function', 'inheritance', 'polymorhism',
         'factorial', 'modulus', 'fibonacci', 'compiler', 
         'debugger', 'computer', 'quantum', 'intelligence']

secret = random.choice(words)

print(secret)

print(secret[0], end='')
print('_' * (len(secret) - 2), end='')
print(secret[-1])