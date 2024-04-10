
def transform(lst: list[int], n: int) -> list[int]:
    result = []

    for i in range(n - 1):
        for j in range(n - i - 1):
            k = i + j
            result.append(max(lst[j:k+1]))

    return result[::-1]


def TransformTransform(a: list[int], n: int) -> bool:
    first = transform(a, n)
    second = transform(first, len(first))

    return sum(second) % 2 == 0

