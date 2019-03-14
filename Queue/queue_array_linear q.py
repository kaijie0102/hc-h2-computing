# Implementation of the Queue ADT (linear_queue) using an array.


class Queue:
    """ Array-based queue implementation (linear_queue)"""

    DEFAULT_CAPACITY = 10  # Class variable applies to all queues
    
    def __init__(self):
        self.items = [None] * Queue.DEFAULT_CAPACITY
        self.rear = -1
        self.size = 0



    def enqueue(self, newItem):
        """Adds newItem to the rear of queue.
        Precondition: the queue is not full."""
        if self.size == Queue.DEFAULT_CAPACITY:
            print("Array is full!")
            return ''
        
        else:
            self.size += 1
            self.rear += 1
            self.items[self.rear] = newItem

    def dequeue(self):
        """Removes and returns the item at front of the queue.
        Precondition: the queue is not empty."""
        if self.size == 0:
            print("List is empty")
            return ''
        else:
            removedItem = self.items[0]

            for i in range(self.size - 1):
                self.items[i] = self.items[i+1]
            self.size -= 1
            self.rear -= 1
            return removedItem


        

    def peek(self):
        """Returns the item at front of the queue.
        Precondition: the queue is not empty."""
        if self.size == 0:
            print("List is empty")
            return ''
        else:
            return self.items[0]
        

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
        for i in range (self.size):
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
