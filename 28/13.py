def UFO(N: int, data: list, octal: bool):
    if octal:
        base = 8
    else:
        base = 16

    for i in range(len(data)):
        data[i] = int(str(data[i]), base)

    return data

