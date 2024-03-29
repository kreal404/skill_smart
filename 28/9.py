def text_to_matrix(s: str, encode: bool) -> list:
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


def transpose_matrix(matrix: list, rows: int, columns: int) -> list:
    transposed_matrix = []
    for column in range(columns):
        transposed_matrix.append([matrix[row][column] for row in range(rows) if column < len(matrix[row])])
    return transposed_matrix


def matrix_to_text(matrix: list, encode: bool) -> str:
    if encode:
        result = " ".join(["".join(row) for row in matrix])
    else:
        result = "".join(["".join(row) for row in matrix])

    return result


def TheRabbitsFoot(s: str, encode: bool) -> str:
    if encode and not s.strip():
        return ""

    matrix = text_to_matrix(s, encode)
    rows = len(matrix)
    columns = len(matrix[0])

    transposed_matrix = transpose_matrix(matrix, rows, columns)

    result = matrix_to_text(transposed_matrix, encode)

    return result

