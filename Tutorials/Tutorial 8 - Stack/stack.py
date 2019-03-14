"""
File: stack.py

Stack implementations
"""

class Array(object):
    """Represents an array."""

    def __init__(self, capacity, fillValue = None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
        self._items = list()
        for count in range(capacity):
            self._items.append(fillValue)
     
    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index."""
        self._items[index] = newItem
        
    def __getitem__(self, index):
            """Subscript operator for access at index."""
            return self._items[index]    



class ArrayStack(object):
    """ Array-based stack implementation."""

    DEFAULT_CAPACITY = 30  # Class variable for all array stacks
    
    def __init__(self):
        self._items = Array(ArrayStack.DEFAULT_CAPACITY)
        self._top = -1
        self._size = 0

    def push(self, newItem):
        """Inserts newItem at top of stack.
        Precondition: the stack is not full."""
        if self._size == ArrayStack.DEFAULT_CAPACITY:
            print ("Stack is full. Abort operation!!")
        else:
            # newItem goes at logical end of array
            self._top += 1
            self._size += 1
            self._items[self._top] = newItem

    def pop(self):
        """Removes and returns the item at top of the stack.
        Precondition: the stack is not empty."""
        if self.isEmpty():
            print ("Stack is empty. Abort operation!!")
        else:
            oldItem = self._items[self._top]
            self._top -= 1
            self._size -= 1
            return oldItem

    def peek(self):
        """Returns the item at top of the stack.
        Precondition: the stack is not empty."""
        if self.isEmpty():
            print ("Stack is empty. Abort operation!!")
        else:
            return self._items[self._top]

    def __len__(self):
        """Returns the number of items in the stack."""
        return self._size
    
    def isEmpty(self):
        return len(self) == 0
    
    def __str__(self):
        """Items strung from bottom to top."""
        result = ""
        for i in range(len(self)):
            result += str(self._items[i]) + " "
        return result

