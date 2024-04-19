def rotate(data: list[int], i: int) -> None:
    data[i], data[i + 1], data[i + 2] = data[i + 1], data[i + 2], data[i]

def MisterRobot(N: int, data: list[int]) -> bool:
    while True:
        for i in range(N - 2):
            if data[i] > data[i + 1]:
                rotate(data, i)
                break
        else:
            break

    return data == sorted(data)

