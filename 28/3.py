def ConquestCampaign(N, M, L, battalion):
    field = []
    day = 1
    cell = 0

    for i in range(N):
        field.append([0]*M)
    for j in range(0, len(battalion), 2):
        field[battalion[j]-1] [battalion[j+1]-1] = 1
        cell += 1
    day += 1
    
    while cell != N*M:
        for r in range(len(field)):
            for c in range(len(field[r])):
                if field[r][c] == 1:
                    if c-1 >= 0 and field[r][c-1] == 0:
                        field[r][c-1] = 1
                        cell += 1
                    if c+1 < M and field[r][c+1] == 0:
                        field[r][c+1] = 1
                        cell += 1
                    if r-1 >= 0 and field[r-1][c] == 0:
                        field[r-1][c] = 1
                        cell += 1
                    if r+1 < N and field[r+1][c] == 0:
                        field[r+1][c] = 1
                        cell += 1
        if cell == M*N:
            break
        day += 1

    return day


