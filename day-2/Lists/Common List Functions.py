nums = [3, 1, 4, 1, 5, 9]

print(len(nums))          # 6
print(max(nums))          # 9
print(min(nums))          # 1
print(sum(nums))          # 23

nums.append(7)            # add at end
print(nums)               # [3,1,4,1,5,9,7]

nums.insert(2, 99)        # insert at index
print(nums)

nums.remove(1)            # remove first occurrence of 1
print(nums)

nums.pop()                # remove last item
print(nums)

nums.sort()               # sort ascending
print(nums)

nums.reverse()            # reverse list
print(nums)




nums = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(nums))
print(unique)  # [1, 2, 3, 4, 5]
