import random

dict = {}

while len(dict) < 100:
    key = random.randint(1, 100)
    value = str(random.randint(1, 100))
    dict[key] = value

for key in dict:
    print(f'{key}: {dict[key]}')

dict.clear()