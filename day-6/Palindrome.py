def is_palindrome(s):
    return s == s[::-1]


print(is_palindrome("121"))  
print(is_palindrome("hello"))
