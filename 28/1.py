def squirrel(N):
    factorial = 1
    while N > 1:
        factorial *= N
        N -= 1
        
    first_digit = int(str(factorial)[0])
    return first_digit

N = 6
print(squirrel(N))