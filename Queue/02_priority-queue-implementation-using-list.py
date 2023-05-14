'''priority queue implementation using list'''
'''Lowest element-->Highest priority or highest element-->highest priority'''

Queue=[]
Queue.append(10)
Queue.append(20)
Queue.append(70)
Queue.append(40)
print('Before sorting :',Queue)
Queue.sort(reverse=True)
print('After sorting :',Queue)
Queue.pop(0)
print(Queue)
Queue.pop(0)
Queue.pop(0)
Queue.pop(0)
print(Queue)

'''output:
Before sorting : [10, 20, 70, 40]
After sorting : [70, 40, 20, 10]
[40, 20, 10]
[]'''