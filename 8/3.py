def list_length(lst: list) -> int:
    if not lst:
        return 0
    lst.pop(0)
    return 1 + list_length(lst)