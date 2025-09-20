def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# test
arr = [10, 20, 30, 40, 50, 60]
print(binary_search(arr, 40))  # 3
print(binary_search(arr, 100)) # -1
