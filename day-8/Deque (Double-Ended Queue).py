from collections import deque

dq = deque()


dq.append(10)     
dq.appendleft(5)   
dq.append(20)

print("Deque:", dq)

print("Removed right:", dq.pop())
print("Removed left:", dq.popleft())
print("Deque after removals:", dq)
