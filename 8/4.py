def is_palindrome(s: str) -> bool:
    s = s.lower()
    if len(s) < 2:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])