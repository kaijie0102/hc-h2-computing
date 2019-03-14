# Implementation of the Queue ADT (circular_queue) using an array.


class Queue:
    """ Array-based queue implementation (circular_queue)"""

    DEFAULT_CAPACITY = 10  # Class variable applies to all queues
    
    def __init__(self):
        self.items = [None] * Queue.DEFAULT_CAPACITY
        self.size = 0
        self.front = 0
        self.rear = -1


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
       


    def dequeue(self):
        """Removes and returns the item at front of the queue.
        Precondition: the queue is not empty."""
        if self.isEmpty():
            print("The list is full!")
            return ''
        else:
            removedItem = self.items[self.front]
            
            if self.front == Queue.DEFAULT_CAPACITY - 1:
                self.items[self.front] = None
                self.front = 0
                
            else:
                self.items[self.front] = None
                self.front += 1

            self.size -= 1
            return removedItem
            
    

    def peek(self):
        """Returns the item at front of the queue.
        Precondition: the queue is not empty."""
        return self.items[self.front]

        

    def __len__(self):
        """Returns the number of items in the queue."""
        return self.size



      
    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False



    def isFull(self):
        if self.size == Queue.DEFAULT_CAPACITY:   
            return True
        else:
            return False



       
    def __str__(self):
        """Items strung from front to rear."""
        string = ''
        for i in range(self.front, self.size):
            if self.front == self.size:
                self.front = 0
            else:
                string += str(self.items[i])
        return string
        




#------------------------------------------------------------------#

def main():
    q = Queue()
    print ("Length:", len(q))
    print ("Empty:", q.isEmpty())
    print ("Enqueue 1-10")
    for i in range(10):
        q.enqueue(i + 1)
    print ("Peeking:", q.peek())
    print ("Items (front to rear):", q)
    print ("Length:", len(q))
    print ("Empty:", q.isEmpty())

    print ('-'*60)
    
    print ("Enqueue 11")
    q.enqueue(11)
    print ("Dequeuing items (front to rear):", end = ' ')
    while not q.isEmpty():
        print (q.dequeue(), end = ' ')
    print ("\nLength:", len(q))
    print ("Empty:", q.isEmpty())
    input('\nPlease press Enter or Return to quit the program.')

main()
