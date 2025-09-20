def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i   # return index
    return -1          # not found

# test
arr = [10, 25, 30, 42, 50]
print(linear_search(arr, 30))  # 2
print(linear_search(arr, 99))  # -1
