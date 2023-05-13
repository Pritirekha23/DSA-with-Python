from collections import deque

def create_stack():
    stack=deque()
    return stack

def push(stack,data):
    stack.append(data)

def pop(stack):
    if stack:
        print('Element deleted')
        print(stack.pop())
        
    else:
        print('stack is empty')
        
def display(stack):
    print('stack elements are::')
    print(stack)
    
new_stack=create_stack()
push(new_stack,10)
push(new_stack,20)
push(new_stack,30)
pop(new_stack)
display(new_stack)
    