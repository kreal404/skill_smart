def Football(F: list[int], N: int) -> bool:
    sorted_F: list[int] = sorted(F)
    diff_indices: list[int] = [i for i in range(N) if F[i] != sorted_F[i]]
    
    if len(diff_indices) == 2:
        return True
    elif len(diff_indices) > 2:
        return diff_indices == list(range(min(diff_indices), max(diff_indices) + 1))
    
    return False

