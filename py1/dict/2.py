import random

def find_duplicates(N):
    lst = []
    for i in range(100):
        lst.append(random.randint(1, 10))

    counts = {}

    for num in lst:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    result = []
    for num, count in counts.items():
        if count >= N:
            result.append(num)
    
    return result

duplicates = find_duplicates(3)

print(duplicates)