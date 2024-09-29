from collections import deque
# the stack implementation is just an array with append() and pop()
q = deque()
# You can add an element to the right with append  
q.append('first')
q.append('second')
q.append('third')
q.appendleft('zero')
print(q)
# You can remove an element to the left with popleft()
q.popleft()

print(q)
