#CIRCULAR QUEUE:

class CQueue():
    def __init__(self,size):
        self.size=size
        self.queue=[None]*size
        self.front=self.rear=-1
        
    def enQueue(self,ele):
        if ((self.rear+1) % self.size== self.front):
            print('Circular queue is full')
        elif (self.front==-1):
            self.front=0
            self.rear=0
            self.queue[self.rear]=ele
            
        else:
            self.rear=(self.rear+1) %self.size
            self.queue[self.rear]=ele
    
    def deQueue(self):
        if(self.front==-1):
            print('Circular queue is empty')
        elif (self.front==self.rear):
            temp=self.queue[self.front]
            self.front=self.rear=-1
            return temp
        else:
            temp=self.queue[self.front]
            self.front=(self.front+1)%self.size
            return temp

    def displayCqueue(self):
        if(self.front==-1):
            print('Circular queue does not have any element')
        elif (self.rear>=self.front):
            for i in range(self.front,  self.rear+1):
              print(self.queue[i],end='')
            print()
        else:
            for i in range(self.front,self.size):
               print(self.queue[i],end='')
            for i in range(0,self.rear+1):
               print(self.queue[i],end='')
            print()
        
obj=CQueue(5)
obj.enQueue(10)
obj.enQueue(20)
obj.enQueue(30)
obj.enQueue(40)
obj.enQueue(50)
print('Queue is:')
obj.displayCqueue()

obj.deQueue()
obj.deQueue()

print('After deletion Queue is:')
obj.displayCqueue()
