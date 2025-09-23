def floor_ceil(arr, target):
    left, right = 0, len(arr) - 1
    floor = None
    ceil = None
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return arr[mid], arr[mid]  # floor = ceil = target
        elif arr[mid] < target:
            floor = arr[mid]
            left = mid + 1
        else:
            ceil = arr[mid]
            right = mid - 1
            
    return floor, ceil

# Example
arr = [1, 3, 5, 6, 8]
target = 4
print(floor_ceil(arr, target))  # Output: (3, 5)
