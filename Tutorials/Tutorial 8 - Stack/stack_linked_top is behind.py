q# Implementation of the Stack ADT using a singly linked list.
               
# The private storage class for creating stack nodes.
class StackNode:
    def __init__(self, item, link) :
        self.data = item
        self.next = link

class Stack:
    """ Link-based stack implementation."""
    
    # Creates an empty stack.
    def __init__(self):
        self.top = None
        self.size = 0
 
    # Returns True if the stack is empty or False otherwise.
    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    # Returns the number of items in the stack.
    def __len__(self):
        return self.size

    # Returns the top item on the stack without removing it.
    def peek(self):
        if self.isEmpty():
            print('Stack is empty')
            return ''
        else:
            cur = self.top
            for i in range(self.size):
                cur = cur.next
            return cur.data
     
    # Removes and returns the top item on the stack.
    def pop(self):
        if self.isEmpty():
            print('Stack is empty')
            return ''
        elif (self.size == 1):
            self.top = None
        else:
            cur = self.top
            for i in range(self.size-1): #go to second last node
                cur = cur.next
            cur.next = None
            self.size -= 1
            return cur.data

    # Pushes an item onto the top of the stack.
    def push(self, item):
        newNode = StackNode(item,None)
        if self.size == None:
            self.top = newNode
        else:
            cur = self.top
            for i in range(self.size):
                cur = cur.next
                cur.next = newNode
        self.size += 1
      
def main():
    
    s = Stack()

    print ("Length:", len(s))
    print ("Empty:", s.isEmpty())
    print ("Popping items (top to bottom):", end = ' ')
    print (s.pop())

    print ('--------------------------------------')
    print ("Push 1-10")
    for i in range(10):
        s.push(i + 1)
    print ("Peeking:", s.peek()) 
    print ("Length:", len(s))
    print ("Empty:", s.isEmpty())
    
    print ('--------------------------------------')
    print ("Push 11")
    s.push(11)
    print ("Popping items (top to bottom):", end = ' ')
    while not s.isEmpty():
        print (s.pop(), end = ' ')
    print ("\nLength:", len(s))
    print ("Empty:", s.isEmpty())
    

main()

