def Football(F, N):
    sorted_F = sorted(F)
    diff_indices = [i for i in range(N) if F[i] != sorted_F[i]]

    if len(diff_indices) == 2:
        return True
    if len(diff_indices) > 2:
        return F == sorted_F

    return False

