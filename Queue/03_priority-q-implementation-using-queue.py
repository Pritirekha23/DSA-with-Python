
import queue
q=queue.PriorityQueue()
q.put(10)
q.put(20)
q.put(30)
q.put(40)

print(q.get())
print(q.get())
print(q.get())
print(q.get())

# Q=[]
# Q.append((1,'Jimin'))
# Q.append((10,'Jin'))
# Q.append((2,'Suga'))
# Q.sort(reverse=True)
# print(Q)

'''output: [(10, 'Jin'), (2, 'Suga'), (1, 'Jimin')]'''
