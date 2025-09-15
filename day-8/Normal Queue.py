from collections import deque

# Normal Queue
queue = deque()

# Enqueue
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue:", queue)

# Dequeue
print("Removed:", queue.popleft())
print("Queue after dequeue:", queue)
