def enqueue(self, newItem):
        """Adds newItem to the rear of queue.
        Precondition: the queue is not full."""
        if self.isFull():
            print("The list is full!")
            return ''
        else:
            if self.rear == Queue.DEFAULT_CAPACITY - 1:     #if rear is the last index, set it to the front
                self.rear = 0
            else:
                self.rear +=1
                
            self.items[self.rear] = newItem
            self.size += 1
'''

        if self.rear == len(self.items) - 1:
                self.rear = 0
        else:
                self.rear += 1
'''    
