def fibonacci(n):
    if n == 0:  # base case
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# 🔍 Test
print(fibonacci(0))  # 0
print(fibonacci(1))  # 1
print(fibonacci(5))  # 5
print(fibonacci(6))  # 8
