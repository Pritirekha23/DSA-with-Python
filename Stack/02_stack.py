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
        print('Element deleted from the top of the stack')
        a=stack.pop() 
        print('Present elements in the stack are:',stack)
 
 
n=int(input('Limit of stack::'))        
while True:
    print('Select the operations :: \n1.push \n 2.pop\n 3.Exit\n ')
    choice=int(input('Choose any one of the above operations::'))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print('Invalid choice please choose a valid number from 1,2 or 3')
        
        
        
        '''OUTPUT::
        Limit of stack::5
Select the operations :: 
1.push 
 2.pop
 3.Exit
 
Choose any one of the above operations::1
Enter the data::10
Present elements in the stack are: ['10']
Select the operations :: 
1.push 
 2.pop
 3.Exit
 
Choose any one of the above operations::1
Enter the data::'RAm'
Present elements in the stack are: ['10', "'RAm'"]
Select the operations :: 
1.push 
 2.pop
 3.Exit
 
Choose any one of the above operations::1
Enter the data::0.2
Present elements in the stack are: ['10', "'RAm'", '0.2']
Select the operations :: 
1.push 
 2.pop
 3.Exit
 
Choose any one of the above operations::1     
Enter the data::233
Present elements in the stack are: ['10', "'RAm'", '0.2', '233']
Select the operations ::
1.push
 2.pop
 3.Exit

Choose any one of the above operations::1     
Enter the data::24
Present elements in the stack are: ['10', "'RAm'", '0.2', '233', '24']
Select the operations ::
1.push
 2.pop
 3.Exit

Choose any one of the above operations::1     
stack is full
Select the operations ::
1.push
 2.pop
 3.Exit

Choose any one of the above operations::2     
Element deleted from the top of the stack     
Present elements in the stack are: ['10', "'RAm'", '0.2', '233']
Select the operations ::
1.push
 2.pop
 3.Exit

Choose any one of the above operations::2     
Element deleted from the top of the stack     
Present elements in the stack are: ['10', "'RAm'", '0.2']
Select the operations ::
1.push
 2.pop
 3.Exit

Choose any one of the above operations::2     
Element deleted from the top of the stack     
Present elements in the stack are: ['10', "'RAm'"]
Select the operations ::
1.push
 2.pop
 3.Exit

Choose any one of the above operations::2     
Element deleted from the top of the stack     
Present elements in the stack are: ['10']     
Select the operations ::
1.push
 2.pop
 3.Exit

Choose any one of the above operations::34    
Invalid choice please choose a valid number from 1,2 or 3
Select the operations ::
1.push
 2.pop
 3.Exit

Choose any one of the above operations::3
          '''
    