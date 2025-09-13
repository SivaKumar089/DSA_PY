def is_palindrome(s):
    return s == s[::-1]

# Test
print(is_palindrome("121"))  # True
print(is_palindrome("hello"))  # False
