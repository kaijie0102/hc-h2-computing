class Stack():

    DEFAULT_CAPACITY = 10

    def __init__(self):
        self.items = [None] * Stack.DEFAULT_CAPACITY    
        self.size = 0
        self.top = -1

    # Check if list is empty
    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False
    
    # Check if list is full
    def isFull(self):
        if self.size == Stack.DEFAULT_CAPACITY:
            return True
        else:
            return False

    # Return size of stack
    def __len__(self):
        return self.size

    # Returns the top item on the stack without removing it
    def peek(self):
        if self.isEmpty():
            print('Stack is empty! Abort operations')
            return ''
        else:
            item=self.items[self.top]
            return item


    # Removes and return the top item of the stack
    def pop(self):
        if self.isEmpty():
            print('Stack is empty! Abort operations')
            return ''
        else:
            item = self.items[self.top]
            self.top -= 1 #decreasing the index of top
            self.size -= 1 #reducing size
            return item

    # Add an item to the top of the stack
    def push(self, item):
        if self.isFull():
            print('Stack is full! Abort operations')
        else:
            self.top += 1
            self.size += 1
            self.items[self.top] = item
            return ''

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
                      





        























                  
        
