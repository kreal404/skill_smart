def power(n: int, m: int) -> int:
    if m == 0:
        return 1
    return n * power(n, m - 1)