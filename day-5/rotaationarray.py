def left_rotate(arr, k):
    k = k % len(arr)
    return arr[k:] + arr[:k]

print(left_rotate([1, 2, 3, 4, 5], 2))  # [3,4,5,1,2]
