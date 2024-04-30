def print_evens(lst: list, i: int) -> None:
    if i >= len(lst):
        return

    if lst[i] % 2 == 0:
        print(lst[i])
    print_evens(lst, i+1)
