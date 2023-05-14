'''(dt-14/05/2023)Queue implementation using List'''

Q=[]

def enQueue():
    if len(Q)==n:
        print('Queue is full')
    else:
        element=int(input('Enter the Element:'))
        Q.append(element)
        print(f'{element} is added to the Queue')
    
def deQueue():
    if Q==[]:
        print('Queue is empty:')
    else:
        e=Q.pop(0)
        print(f'{e} is removed from the Queue')
        
        
def front():
    if Q==[]:
        print('Queue is Empty')
    else:
        print(Q[0])
        
def display():
    print('Elements present in the Queue are:',Q)
    
n=int(input('Limit of Queue:'))     
while True:
    print('Select the operation \n 1.enqueue\n 2.deQueue\n 3.front\n 4.display\n 5.Exit')
    choice=int(input('Choose any one from the above:'))
    if choice==1:
        enQueue()
    elif choice==2:
        deQueue()
    elif choice==3:
        front()
    elif choice==4:
        display()
    elif choice==5:
        break
    else:
        print('Invalid choice please choose a valid option')
        
        
'''output
Limit of Queue:3
Select the operation 
 1.enqueue
 2.deQueue
 3.front
 4.display
 5.Exit
Choose any one from the above:1
Enter the Element:27
27 is added to the Queue
Select the operation 
 1.enqueue
 2.deQueue
 3.front
 4.display
 5.Exit
Choose any one from the above:1
Enter the Element:356
356 is added to the Queue
Select the operation 
 1.enqueue
 2.deQueue
 3.front
 4.display
 5.Exit
Choose any one from the above:1
Enter the Element:53
53 is added to the Queue
Select the operation 
 1.enqueue
 2.deQueue
 3.front
 4.display
 5.Exit
Choose any one from the above:1
Queue is full
Select the operation
 1.enqueue
 2.deQueue
 3.front
 4.display
 5.Exit
Choose any one from the above:3
27
Select the operation
 1.enqueue
 2.deQueue
 3.front
 4.display
 5.Exit
Choose any one from the above:2
27 is removed from the Queue
Select the operation
 1.enqueue
 2.deQueue
 3.front
 4.display
 5.Exit
Choose any one from the above:2
356 is removed from the Queue
Select the operation
 1.enqueue
 2.deQueue
 3.front
 4.display
 5.Exit
Choose any one from the above:2
53 is removed from the Queue
Select the operation
 1.enqueue
 2.deQueue
 3.front
 4.display
 5.Exit
Choose any one from the above:2
Queue is empty:
Select the operation
 1.enqueue
 2.deQueue
 3.front
 4.display
 5.Exit
Choose any one from the above:3
Queue is Empty
Select the operation
 1.enqueue
 2.deQueue
 3.front
 4.display
 5.Exit
Choose any one from the above:1
Enter the Element:45
45 is added to the Queue
Select the operation
 1.enqueue
 2.deQueue
 3.front
 4.display
 5.Exit
Choose any one from the above:1
Enter the Element:43
43 is added to the Queue
Select the operation
 1.enqueue
 2.deQueue
 3.front
 4.display
 5.Exit
Choose any one from the above:1
Enter the Element:53
53 is added to the Queue
Select the operation
 1.enqueue
 2.deQueue
 3.front
 4.display
 5.Exit
Choose any one from the above:4
Elements present in the Queue are: [45, 43, 53]
Select the operation
 1.enqueue
 2.deQueue
 3.front
 4.display
 5.Exit
Choose any one from the above:5'''