def generate_parentheses(n, open_brackets, close_brackets, s):
    if open_brackets == n and close_brackets == n:
        print(s)
        return

    if open_brackets < n:
        generate_parentheses(n, open_brackets + 1, close_brackets, s + '(')

    if close_brackets < open_brackets:
        generate_parentheses(n, open_brackets, close_brackets + 1, s + ')')
