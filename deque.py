from collections import deque

queue = deque([5])

queue.append(4)
queue.append(3)
queue.append(2)
queue.append(1)
queue.popleft()
queue.append(2)
queue.append(3)

print(queue)