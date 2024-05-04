def is_palindrome(s):
    def helper(start, end):
        if start >= end:
            return True
        if s[start] != s[end]:
            return False
        return helper(start + 1, end - 1)
    return helper(0, len(s) - 1)
