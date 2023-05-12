stack=[]

def push():
    if len(stack)==n:
        print('stack is full')
    else:
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
 
n=int(input('Limit of stack::'))        
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
        Limit of stack::4
Select the operations :: 
1.push 
 2.pop
 3.Exit
 
Select any one of the above operations::1
Enter the data::20
Present elements in the stack are: ['20']
Select the operations :: 
1.push 
 2.pop
 3.Exit
 
Select any one of the above operations::1
Enter the data::30
Present elements in the stack are: ['20', '30']
Select the operations :: 
1.push 
 2.pop
 3.Exit
 
Select any one of the above operations::1
Enter the data::40
Present elements in the stack are: ['20', '30', '40']
Select the operations :: 
1.push 
 2.pop
 3.Exit
 
Select any one of the above operations::1     
Enter the data::50
Present elements in the stack are: ['20', '30', '40', '50']
Select the operations ::
1.push
 2.pop
 3.Exit

Select any one of the above operations::1     
stack is full
Select the operations ::
1.push
 2.pop
 3.Exit

Select any one of the above operations::2     
Element deleted from the top of the stack     
Present elements in the stack are: ['20', '30', '40']
Select the operations ::
1.push
 2.pop
 3.Exit

Select any one of the above operations::2     
Element deleted from the top of the stack     
Present elements in the stack are: ['20', '30']
Select the operations ::
1.push
 2.pop
 3.Exit

Select any one of the above operations::2     
Element deleted from the top of the stack     
Present elements in the stack are: ['20']     
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

Select any one of the above operations::2     
Stack is Empty
Select the operations ::
1.push
 2.pop
 3.Exit

Select any one of the above operations::3  '''
    