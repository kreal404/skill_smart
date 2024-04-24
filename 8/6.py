def print_even_index(lst: list[int], i: int = 0) -> None:
    if i < len(lst):
        print(lst[i])
        print_even_index(lst, i + 2)
