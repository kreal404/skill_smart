def is_palindrome(s: str, start: int, end: int) -> bool:
    s = s.lower()
    if start >= end:
        return True
    elif s[start] != s[end]:
        return False
    return is_palindrome(s, start + 1, end - 1)
