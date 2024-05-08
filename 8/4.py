def is_palindrome(s):
    s = s.lower()
    return helper(s, 0, len(s) - 1)

def helper(s, start, end):
    if start >= end:
        return True
    if s[start] != s[end]:
        return False
    return helper(s, start + 1, end - 1)

