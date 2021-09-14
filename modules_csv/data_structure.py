class CircularQueue:
    # The Circular queue which is designed to contain lists.
    def __init__(self, queue_size):
        self.__queue = []
        self.__QUEUE_SIZE = queue_size + 1
        self.__rear = 0
        self.__front = 0
        for a in range(self.__QUEUE_SIZE):
            self.__queue.append([])
        # if continor of queue is enpty list([]), it means that containor is empty.
    
    def IsEmpty(self):
        if self.__rear == self.__front:
            return True
        else:
            return False
    
    def IsFull(self):
        if (self.__rear+1)%self.__QUEUE_SIZE == self.__front:
            return True
        else:
            return False
    
    def Enqueue(self, param_data):
        if self.IsFull():
            raise Exception("Queue is full. Can't enqueue data.")
        
        self.__rear = (self.__rear + 1) % self.__QUEUE_SIZE
        self.__queue[self.__rear] = param_data
    
    def Dequeue(self):
        if self.IsEmpty():
            raise Exception("Queue is empty. Can't dequeue data")

        self.__front = (self.__front + 1) % self.__QUEUE_SIZE
        return self.__queue[self.__front]
    
    def Top(self): # Get data of rear. Same as in case of stack.
        if self.IsEmpty():
            raise Exception("Queue is empty. Can't get data of top.")
        return self.__queue[self.__rear]
    
    def Pop(self): # Get data of rear and remove data of rear. Same as in case of stack.
        if self.IsEmpty():
            raise Exception("Queue is empty. Can't pop data.")
        
        to_return = self.__queue[self.__rear]
        self.__rear = (self.__rear + self.__QUEUE_SIZE -1) % self.__QUEUE_SIZE
        return to_return