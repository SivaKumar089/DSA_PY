def subarray_sum(nums, target):
    prefix_sum = 0
    seen = set()  # store prefix sums
    for num in nums:
        prefix_sum += num

        if prefix_sum == target or (prefix_sum - target) in seen:
            return True

        seen.add(prefix_sum)

    return False

# Example
nums = [10, 2, -2, -20, 10]
target = -10
print(subarray_sum(nums, target))  # Output: True
