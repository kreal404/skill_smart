def text_to_matrix(s: str, encode: bool) -> list[list[str]]:
    if encode:
        s = s.replace(" ", "")
        n = len(s)

        sqrt_n = n ** .5
        rows = int(sqrt_n)
        columns = int(sqrt_n) + 1

        while rows * columns < n:
            rows += 1

        matrix = [list(s[i:i + columns]) for i in range(0, n, columns)]
    else:
        matrix = [list(word) for word in s.split()]

    return matrix


def transpose_matrix(matrix: list[list[str]], rows: int, columns: int) -> list[list[str]]:
    transposed_matrix = []
    for column in range(columns):
        transposed_matrix.append([matrix[row][column] for row in range(rows) if column < len(matrix[row])])

    return transposed_matrix


def matrix_to_text(matrix: list[list[str]]) -> str:
    return " ".join(["".join(row) for row in matrix])


def TheRabbitsFoot(s: str, encode: bool) -> str:
    matrix = text_to_matrix(s, encode)
    rows = len(matrix)
    columns = len(matrix[0])

    transposed_matrix = transpose_matrix(matrix, rows, columns)

    result = matrix_to_text(transposed_matrix)

    return result

