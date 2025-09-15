from collections import deque

dq = deque()

# Insert at both ends
dq.append(10)        # right
dq.appendleft(5)     # left
dq.append(20)

print("Deque:", dq)

# Remove from both ends
print("Removed right:", dq.pop())
print("Removed left:", dq.popleft())
print("Deque after removals:", dq)
