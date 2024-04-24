def second_max(lst: list, max1: int = None, max2: int = None) -> int:
    if not lst:
        return max2

    if max1 is None or lst[0] >= max1:
        max1, max2 = lst[0], max1

    elif max2 is None or max1 >= lst[0] >= max2:
        max2 = lst[0]

    return second_max(lst[1:], max1, max2)
