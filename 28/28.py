def Keymaker(k: int) -> str:
    doors = [0] * k

    for i in range(k):
        for j in range(i, k, i+1):
            doors[j] = 1 - doors[j]

    return ''.join(map(str, doors))

