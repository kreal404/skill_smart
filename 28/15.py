def TankRush(H1: int, W1: int, S1: str, H12: int, W2: int, S2: str) -> bool:
    total_map = S1.split()
    tanks_map = S2.split()
    count = 0

    for i in tanks_map:
        for j in total_map:
            if i in j:
                count += 1
                break

    return count == len(tanks_map)

