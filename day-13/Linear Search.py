def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1          

arr = [10, 25, 30, 42, 50]
print(linear_search(arr, 30))  
print(linear_search(arr, 99))  