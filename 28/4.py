def MadMax(N: int, Tele: list) -> list:
    Tele.sort()
    result = [0] * N

    left_idx = 0
    right_idx = N - 1

    for i in range(0, N // 2):
        result[i] = Tele[left_idx]
        left_idx += 1

    for i in range(N // 2, N):
        result[i] = Tele[right_idx]
        right_idx -= 1

    return result


