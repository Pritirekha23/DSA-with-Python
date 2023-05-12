''' STACK ::
    Stack is a linear Data structure, in which opearations( like insertion and deletion) are done at one end known as top. It is used to store data. It obeys a particular order that is FILO(First-In-Last-Out) or LIFO(LAst-In-First-Out).
    OPERATIONS:
     PUSH()-Insert data into stack
     POP()-remove data from stack
     TOP() or PEEK()-Returns top element of the stack
     SIZE() or COUNT()-Returns total number of elements stored in the stack
     isEmpty()-Check whether any element are stored in the stack or not  so if the stack is empty then pop() and top() operation can not be performed that is called as UNDERFLOW.
     isFull()-It Checks whether the stack is full or not , if the stack is full then push() operation cant be perfomed that is called as OVERFLOW.'''
     
#We can implement stack using list and modules.
#STACK IMPLEMETATION USING LIST    
 
stack=[]

def push():
    if len(stack)==n:
        print('stack is full')
    else:
        data=input('Enter the data::')
        stack.append(data)
        
    
def pop():
    if  stack==[]:
        print('Stack is Empty')
    else:
        print('Element deleted from the top of the stack')
        a=stack.pop() 
        
 
def display():
    print('Present elements in the stack are:',stack)
     
def peek():
    if stack==[]:
        print('Stack is Empty')
    else:
        print(stack[-1])

    
n=int(input('Limit of stack::'))        
while True:
    print('Select the operations :: \n1.push \n 2.pop\n 3.display\n 4.peek\n 5.Exit\n ')
    choice=int(input('Choose any one of the above operations::'))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        display()
    elif choice==4:
        peek()
        
    elif choice==5:
        break
    
    else:
        print('Invalid choice please choose a valid number ')
 

'''output:
Limit of stack::4
Select the operations :: 
1.push 
 2.pop
 3.display
 4.peek
 5.Exit
 
Choose any one of the above operations::1
Enter the data::30
Select the operations :: 
1.push 
 2.pop
 3.display
 4.peek
 5.Exit
 
Choose any one of the above operations::2
Element deleted from the top of the stack
Select the operations :: 
1.push 
 2.pop
 3.display
 4.peek
 5.Exit
 
Choose any one of the above operations::4
Stack is Empty
Select the operations ::
1.push
 2.pop
 3.display
 4.peek
 5.Exit

Choose any one of the above operations::1
Enter the data::priti
Select the operations ::
1.push
 2.pop
 3.display
 4.peek
 5.Exit

Choose any one of the above operations::1
Enter the data::45
Select the operations ::
1.push
 2.pop
 3.display
 4.peek
 5.Exit

Choose any one of the above operations::1
Enter the data::0.3
Select the operations ::
1.push
 2.pop
 3.display
 4.peek
 5.Exit

Choose any one of the above operations::1
Enter the data::65
Select the operations ::
1.push
 2.pop
 3.display
 4.peek
 5.Exit

Choose any one of the above operations::1
stack is full
Select the operations ::
1.push
 2.pop
 3.display
 4.peek
 5.Exit

Choose any one of the above operations::544
Invalid choice please choose a valid number
Select the operations ::
1.push
 2.pop
 3.display
 4.peek
 5.Exit

Choose any one of the above operations::1
stack is full
Select the operations ::
1.push
 2.pop
 3.display
 4.peek
 5.Exit

Choose any one of the above operations::3
Present elements in the stack are: ['priti', '45', '0.3', '65']
Select the operations ::
1.push
 2.pop
 3.display
 4.peek
 5.Exit

Choose any one of the above operations::1
stack is full
Select the operations ::
1.push
 2.pop
 3.display
 4.peek
 5.Exit

Choose any one of the above operations::4
65
Select the operations ::
1.push
 2.pop
 3.display
 4.peek
 5.Exit

Choose any one of the above operations::5
   '''        

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
# stack=[]

# def push():
#     data=input('Enter the data::')
#     stack.append(data)
#     print('Present elements in the stack are:',stack)
    
# def pop():
#     if stack==[]:
#         print('Stack is Empty')
#     else:
#         a=stack.pop()
#         print('Element deleted from the top of the stack')
#         print('Present elements in the stack are:',stack)
        
# while True:
#     print('Select the operations :: \n1.push \n 2.pop\n 3.Exit\n ')
#     choice=int(input('Select any one of the above operations::'))
#     if choice==1:
#         push()
#     elif choice==2:
#         pop()
#     elif choice==3:
#         break
#     else:
#         print('Invalid choice please choose a valid number from 1,2 or 3')
    
    
    
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
 
 
 
 
 