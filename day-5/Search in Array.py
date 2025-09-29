def search_array(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i    
    return -1  

print(search_array([10, 20, 30, 40, 50], 30))  
print(search_array([10, 20, 30, 40, 50], 60))  
