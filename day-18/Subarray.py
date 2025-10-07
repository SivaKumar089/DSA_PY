def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])  # sum of first window
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]  # slide the window
        max_sum = max(max_sum, window_sum)

    return max_sum


arr = [2, 1, 5, 1, 3, 2]
k = 3
print("Maximum sum subarray:", max_sum_subarray(arr, k))
