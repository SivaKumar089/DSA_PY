from collections import deque


queue = deque()


queue.append(10)
queue.append(20)
queue.append(30)

print("Queue:", queue)


print("Removed:", queue.popleft())
print("Queue after dequeue:", queue)
