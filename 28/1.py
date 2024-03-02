def squirrel(N: int) -> int:
    factorial: int = 1
    while N > 1:
        factorial *= N
        N -= 1

    first_digit: int = int(str(factorial)[0])
    return first_digit
