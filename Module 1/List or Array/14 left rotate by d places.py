from collections import deque
l = [10,20,30,40,50]
d = 2
dq = deque(l)
dq.rotate(-d)
l = list(dq)
print(l)

#method 1
def leftrotate(l,d):
  for i in range(0,d):
    l .append(l.pop(0))

#method 2
def reverse(l,b,e):
  while b<e:
    l[b],l[e]=l[e],l[b]
    b = b+1
    e = e-1
def leftRotate(l,d):
  n = len(l)
  reverse(l,0,d-1)
  reverse(l,d,n-1)
  reverse(l,0,n-1)  
