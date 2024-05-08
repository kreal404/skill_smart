def generate_parentheses(n: int) -> list[str]:
    result = []
    helper(n, 0, 0, '', result)
    return result

def helper(n: int, open_brackets: int, close_brackets: int, s:list[str], result:list[str]):
    if open_brackets == close_brackets == n:
        result.append(s)
    else:
        if open_brackets < n:
            helper(n, open_brackets + 1, close_brackets, s + '(', result)
        if close_brackets < open_brackets:
            helper(n, open_brackets, close_brackets + 1, s + ')', result)

