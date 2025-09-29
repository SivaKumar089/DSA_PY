from collections import deque

stack = deque()


stack.append("a")
stack.append("b")
stack.append("c")
print("Stack:", stack)   


print("Popped:", stack.pop()) 
print("Stack after pop:", stack)  
