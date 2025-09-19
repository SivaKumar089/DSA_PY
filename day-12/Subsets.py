def subsets(nums):
    result = []
    
    def backtrack(index, current):
        if index == len(nums):
            result.append(current[:])  # copy
            return
        
        # Exclude nums[index]
        backtrack(index + 1, current)
        
        # Include nums[index]
        current.append(nums[index])
        backtrack(index + 1, current)
        current.pop()  # backtrack
    
    backtrack(0, [])
    return result


# Example
nums = [1, 2, 3]
print(subsets(nums))
