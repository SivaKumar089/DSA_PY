def is_balanced(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():  # opening bracket
            stack.append(char)
        elif char in mapping:  # closing bracket
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return not stack


# Test cases
print(is_balanced("{[()]}"))   # True
print(is_balanced("{[(])}"))   # False
print(is_balanced("((()))"))   # True
