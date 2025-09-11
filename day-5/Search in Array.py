def search_array(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i   # return index
    return -1   # not found

print(search_array([10, 20, 30, 40, 50], 30))  # 2
print(search_array([10, 20, 30, 40, 50], 60))  # -1
