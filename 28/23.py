def TreeOfLife(H, W, N, tree):
    lst_tree = []
    for row in tree:
        temp = []
        for cell in row:
            if cell == '+':
                temp.append(1)
            else:
                temp.append(0)
        lst_tree.append(temp)

    for year in range(N):

        to_remove = []

        for i in range(H):
            for j in range(W):
                if lst_tree[i][j] > 0:
                    lst_tree[i][j] += 1

                if lst_tree[i][j] == 0 and year % 2 == 0:
                    lst_tree[i][j] = 1

                if lst_tree[i][j] >= 3 and year % 2 != 0:
                    to_remove.append((i, j))

        for i, j in to_remove:
            lst_tree[i][j] = 0
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < H and 0 <= nj < W:
                    lst_tree[ni][nj] = 0

    result = []
    for row in lst_tree:
        temp = ''
        for cell in row:
            if cell > 0:
                temp += '+'
            else:
                temp += '.'

        result.append(temp)

    return result

