nums = [3, 1, 4, 1, 5, 9]

print(len(nums))          
print(max(nums))          
print(min(nums))          
print(sum(nums))          

nums.append(7)            
print(nums)               

nums.insert(2, 99)        
print(nums)

nums.remove(1)            
print(nums)

nums.pop()                
print(nums)

nums.sort()               
print(nums)

nums.reverse()            
print(nums)




nums = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(nums))
print(unique) 
