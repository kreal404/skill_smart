def print_even_index(lst: list[int], i: int) -> None:
    if i < len(lst):
        print(lst[i])
        print_even_index(lst, i + 2)
