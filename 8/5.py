def print_evens(lst: list) -> None:
    helper(lst, 0)

def helper(lst: list, index: int) -> None:
    if index >= len(lst):
        return
    if lst[index] % 2 == 0:
        print(lst[index])
    helper(lst, index + 1)

