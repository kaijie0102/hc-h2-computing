from stack import ArrayStack

stk = ArrayStack()

def stackToQueue(stk):
    queue = LinkedQueue():
    temp = LinkedStack()

    while not stack.isEmpty():
        item = stack.pop()
        queue.enqueue(item)
        temp.push(item)

    while not temp.isEmpty():
        stack.push(temp.pop())

    return queue
        
    
        
