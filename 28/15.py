def string_to_list(s: str) -> list:
    result = []

    for row in s.split():
        temp = []
        for n in row:
            temp.append(int(n))
        result.append(temp)

    return result


def TankRush(H1: int, W1: int, S1: str, H2: int, W2: int, S2: str) -> bool:
    total_map = string_to_list(S1)
    tanks_map = string_to_list(S2)

    for i in range(H1 - H2 + 1):
        for j in range(W1 - W2 + 1):
            count = 0
            
            for x in range(H2):
                for y in range(W2):
                    count += total_map[i + x][j + y] == tanks_map[x][y]

            if count == H2 + W2:
                return True

    return False


