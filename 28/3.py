def ConquestCampaign(N, M, L, battalion):
    field = [[0] * M for _ in range(N)]
    day = 1
    cell = 0

    for i in range(0, len(battalion), 2):
        row = battalion[i] - 1
        col = battalion[i+1] - 1
        if field[row][col] == 0:
            field[row][col] = 1
            cell += 1

    while cell != N * M:
        for r in range(N):
            for c in range(M):
                if field[r][c] == 1:
                    if c - 1 >= 0 and field[r][c - 1] == 0:
                        field[r][c - 1] = 1
                        cell += 1
                    if c + 1 < M and field[r][c + 1] == 0:
                        field[r][c + 1] = 1
                        cell += 1
                    if r - 1 >= 0 and field[r - 1][c] == 0:
                        field[r - 1][c] = 1
                        cell += 1
                    if r + 1 < N and field[r + 1][c] == 0:
                        field[r + 1][c] = 1
                        cell += 1

        day += 1

    return day

