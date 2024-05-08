def print_even_index(lst: list[int]) -> None:
    helper(lst, 0)

def helper(lst: list[int], index: int) -> None:
    if index < len(lst):
        print(lst[index])
        helper(lst, index + 2)

