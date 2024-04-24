def is_palindrome(s: str, start: int = 0, end: int = None) -> bool:
    if end is None:
        end = len(s) - 1
    s = s.lower()
    if start >= end:
        return True
    elif s[start] != s[end]:
        return False
    return is_palindrome(s, start + 1, end - 1)
