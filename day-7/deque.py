from collections import deque

stack = deque()

# Push
stack.append("a")
stack.append("b")
stack.append("c")
print("Stack:", stack)   # deque(['a','b','c'])

# Pop
print("Popped:", stack.pop())  # 'c'
print("Stack after pop:", stack)  # deque(['a','b'])
