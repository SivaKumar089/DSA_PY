def sum_of_digits(n):
    if n == 0:   # base case
        return 0
    return (n % 10) + sum_of_digits(n // 10)  # last digit + recursive call

# 🔍 Test
print(sum_of_digits(1234))  # 10
print(sum_of_digits(9876))  # 30
