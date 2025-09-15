from collections import deque

class StackUsingQueue:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        # Rotate to make last pushed at front
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

s = StackUsingQueue()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())  # 30
print(s.pop())  # 20
