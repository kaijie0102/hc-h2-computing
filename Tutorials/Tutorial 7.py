#Linked list
"""
File: remove.py

Define a function named remove that removes the item at a given position,
where 1 <= positon <= lengthOfList

The funciton returns a tuple containing the modified linked structure
and the item that was removed.

"""

class Node(object):

    def __init__(self, data, next = None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next


def length(head):
    """Returns the number of items in the linked structure
    referred to by head."""
    probe = head
    count = 0
    while probe != None:
        count += 1
        probe = probe.next
    return count
    

def insert(index, newItem, head):
    """Inserts newItem at position index in the linked structure
    referred to by head.  Returns a reference to the new
    structure."""

    """Assumes that 1st item is at index 1 """


    newNode = Node(newItem, None)   # create a Node object contains 
                                    # newItem and an empty link
    if index == 1:
        # newItem goes at the head
        newNode.next = head
        head = newNode
    else:
        # Search for the (index-1)th node
        predNode = None
        currNode = head           
        for i in range(index-1):       # loop for (index-1) times 
            predNode = currNode
            currNode = currNode.next
          
        # Insert new node after predecessor
        newNode.next = currNode
        predNode.next = newNode
        
    return head


def remove(index, head):
    """Removes the item at index from the linked structure
    referred to by head and returns the tuple (head, item)"""
    
    """Assumes that the structure has at least one item and
    the 1st item is at index 1"""

    if index == 1:
        removedItem = head.data
        head = head.next
        

    else:    
        c = head
        p = None
        for i in range(index-1):
            p = c
            c = c.next
        removedItem = c.data
        p.next = c.next
        
    return(head, removedItem)


def printStructure(head):
    """Prints the items in the structure referred to by head."""
    probe = head
    while probe != None:
        print (probe.data, end = ' ')
        probe = probe.next
    print ()


def main():
    """Tests modifications."""
    head = None

    head = insert(1, "1", head)
    print ("1:", end = ' ')
    printStructure(head)

    (head, item) = remove(1, head)
    print ("1:", item)
    printStructure(head)

    # Add five nodes to the beginning of the linked structure
    for count in range(1, 5+1):
        head = Node(count, head)
    
    (head, item) = remove(1, head)
    print ("5 4 3 2 1:", item, end = ' ')
    printStructure(head)
    
    (head, item) = remove(length(head), head)
    print ("1 4 3 2:", item, end = ' ')
    printStructure(head)

    (head, item) = remove(2, head)
    print ("3 4 2:", item, end = ' ')
    printStructure(head)

 
main()


"""
File: insert.py

Define a function named insert that inserts an item into a linked structure
at a given position, where 1 <= position <= lengthOfList+1

The function returns the modified linked structure

"""

class Node(object):

    def __init__(self, data, next = None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next

    

def insert(index, newItem, head):
    """Inserts newItem at position index in the linked structure
    referred to by head.  Returns a reference to the new
    structure."""
    newNode = Node(newItem,None)
    """Assumes that 1st item is at index 1 """
    if index == 1:
        newNode.next = head
        head = newNode
        
    else:
        p = None
        c = head
        for i in range(index-1):
            p = c
            c = c.next
        p.next = newNode    
        newNode.next = c
        
        

    return head 



def printStructure(head):
    """Prints the items in the structure referred to by head."""
    probe = head
    while probe != None:
        print (probe.data, end = ' ')
        probe = probe.next
    print ()



def main():
    """Tests modifications."""
    head = None

    head = insert(1, "1", head)
    print ("1:", end = ' ')
    printStructure(head)

    head = insert(2, "2", head)
    print ("1 2:", end = ' ')
    printStructure(head)

    head = insert(1, "0", head)
    print ("0 1 2:", end = ' ')
    printStructure(head)

    head = insert(4, "3", head)
    print ("0 1 2 3:", end = ' ')
    printStructure(head)

    head = insert(2, "9", head)
    print ("0 9 1 2 3:", end = ' ')
    printStructure(head)


main()






"""
File: length.py

Define a function length that returns the number of items in the linked structure

"""

class Node(object):

    def __init__(self, data, next = None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next
        

def length(head):
    """Returns the number of items in the linked structure
    referred to by head."""
    Count = 0
    p = head
    while p != None:
        Count+=1
        p = p.next
    return Count
       
   
def main():
    """Tests modifications."""
    head = None
    print ("0:", length(head))

    # Add five nodes to the beginning of the linked structure
    for count in range(1, 5+1):
        head = Node(count, head)

    print ("5:", length(head))


main()





