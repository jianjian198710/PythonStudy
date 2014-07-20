#10.3.4
from collections import deque
from heapq import *
from random import shuffle


#1.Set
a=set([1,2,3])
b=set([2,3,4])
print "a.union(b) is: "+str(a.union(b))
print "a&b is: "+str(a&b)
print "a-b is: "+str(a-b)
print "a.symmetric_difference(b) is: "+str(a.symmetric_difference(b))
print "a^b is: "+str(a^b)

#2.Heap
data=range(10)
shuffle(data)
heap=[]
for n in data:
    heappush(heap,n)
print "heap is: "+str(heap)
heappush(heap,0.5)
print "heap is: "+str(heap)
print "heappop is: "+str(heappop(heap))
print "heappop is: "+str(heappop(heap))
print "nsmallest is: "+str(nsmallest(2,heap))

#3.Deque
q=deque(range(5))
q.append(5)
q.appendleft(6)
print "deque is: "+str(q)
print "q.pop() is: "+str(q.pop())
print "q.popleft() is: "+str(q.popleft())
print "q.rotate(3) is: "+str(q.rotate(3))
print "q.rotate(-1) is: "+str(q.rotate(-1))