def Football(F, N):
    sorted_F = sorted(F)
    diff_indices = [i for i in range(N) if F[i] != sorted_F[i]]

    if len(diff_indices) == 2 or F[::-1] == sorted_F:
        return True

    return False

