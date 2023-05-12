''' STACK ::
    Stack is a linear Data structure, in which opearations( like insertion and deletion) are done at one end known as top. It is used to store data. It obeys a particular order that is FILO(First-In-Last-Out) or LIFO(LAst-In-First-Out).
    OPERATIONS:
     PUSH()-Insert data into stack
     POP()-remove data from stack
     TOP() or PEEK()-Returns top element of the stack
     SIZE() or COUNT()-Returns total number of elements stored in the stack
     isEmpty()-Check whether any element are stored in the stack or not  so if the stack is empty then pop() and top() operation can not be performed that is called as UNDERFLOW.
     isFull()-It Checks whether the stack is full or not , if the stack is full then push() operation cant be perfomed that is called as OVERFLOW.'''
     
#We can implent stack using list and modules.
#STACK IMPLEMETATION USING LIST    
 
stack=[]

def push():
    data=input('Enter the data::')
    stack.append(data)
    print('Present elements in the stack are:',stack)
    
def pop():
    if not stack:
        print('Stack is Empty')
    else:
        a=stack.pop()
        print('Element deleted from the top of the stack')
        print('Present elements in the stack are:',stack)
        
while True:
    print('Select the operations :: \n1.push \n 2.pop\n 3.Exit\n ')
    choice=int(input('Select any one of the above operations::'))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print('Invalid choice please choose a valid number from 1,2 or 3')
    
    
    
'''OUTPUT::
 Select the operations :: 
1.push 
 2.pop
 3.Exit
 
Select any one of the above operations::1
Enter the data::13
Present elements in the stack are: ['13']
Select the operations :: 
1.push 
 2.pop
 3.Exit
 
Select any one of the above operations::1
Enter the data::23
Present elements in the stack are: ['13', '23']
Select the operations :: 
1.push 
 2.pop
 3.Exit
 
Select any one of the above operations::2
Element deleted from the top of the stack
Present elements in the stack are: ['13']
Select the operations :: 
1.push 
 2.pop
 3.Exit
 
Select any one of the above operations::1
Enter the data::34
Present elements in the stack are: ['13', '34']
Select the operations ::
1.push
 2.pop
 3.Exit

Select any one of the above operations::1     
Enter the data::43
Present elements in the stack are: ['13', '34', '43']
Select the operations ::
1.push
 2.pop
 3.Exit

Select any one of the above operations::2     
Element deleted from the top of the stack     
Present elements in the stack are: ['13', '34']
Select the operations ::
1.push
 2.pop
 3.Exit

Select any one of the above operations::22    
Invalid choice please choose a valid number from 1,2 or 3
Select the operations ::
1.push
 2.pop
 3.Exit

Select any one of the above operations::2     
Element deleted from the top of the stack     
Present elements in the stack are: ['13']     
Select the operations ::
1.push
 2.pop
 3.Exit

Select any one of the above operations::2     
Element deleted from the top of the stack     
Present elements in the stack are: []
Select the operations ::
1.push
 2.pop
 3.Exit

Select any one of the above operations::3 
 '''   
 
 
 
 
 