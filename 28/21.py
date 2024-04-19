def BiggerGreater(input: str):
    input = list(input)

    i = len(input) - 2
    j = len(input) - 1

    while i >= 0 and input[i] >= input[i + 1]:
        i -= 1

    if i == -1:
        return ''

    while input[j] <= input[i]:
        j -= 1

    input[i], input[j] = input[j], input[i]

    input[i + 1:] = reversed(input[i + 1:])

    return ''.join(input)

