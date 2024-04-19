def S(A: list) -> list:
    B = []
    for i in range(len(A)):
        for j in range(len(A) - i):
            k = i + j
            B.append(max(A[j:k+1]))
    return B


def TransformTransform(A, N):
    B = S(S(A))
    return sum(B) % 2 == 0

