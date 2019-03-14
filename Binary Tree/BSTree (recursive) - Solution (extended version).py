# A Binary Search Tree (BST) Example

import random

#========================================================================
class TreeNode:
   def __init__(self, value):
      self.data = value
      self.left = None
      self.right = None
      
#========================================================================
class BSTree:     # binary search tree

   def __init__(self):
      self.root = None


   # Adds new node   
   def insert(self, newValue, tree):    # recursive
      if tree == None:    #  or if self.root == None
         self.root = TreeNode(newValue)
      else:
         if newValue < tree.data:     
            if tree.left == None:
               tree.left = TreeNode(newValue)   
            else:   
               self.insert(newValue, tree.left) 
         else:                 # newValue > tree.data
            if tree.right == None:
               tree.right = TreeNode(newValue)
            else:
               self.insert(newValue, tree.right)

  
   # Looks for a value in the tree   
   # Returns False if not found else returns True
   def search(self, target, tree):      # recursive
      if tree == None:
         return False
      else:
         if target == tree.data:
            return True
         elif target < tree.data:
            return self.search(target, tree.left)   # 'return' is a MUST
         else:           # target > tree.data
            return self.search(target, tree.right)  # 'return' is a MUST

 
   # Gets the root of the tree
   def getRoot(self):
      return self.root


   # Gets the size of the tree, i.e. number of nodes
   def size(self, tree):
      if tree == None:
         return 0
      else:
         return self.size(tree.left) + 1 + self.size(tree.right)


   # Gets the minimum value
   def minValue(self, tree):
      # goes down into the left arm and returns the last value
     
      if tree == None:       # recursive
         return ''
      elif tree.left == None:
         return tree.data
      else:
         return self.minValue(tree.left)
      """
      if tree == None:       # non-recursive 
         return ''
      else:
         cur = tree
         while cur.left != None:
            cur = cur.left
         return cur.data
      """
      

   # Gets the maximum value
   def maxValue(self, tree):
        # goes down into the right arm and returns the last value
        
        if tree == None:      # non-revcursive  
           return ''
        else:
           cur = tree
           while cur.right != None:  
               cur = cur.right
           return cur.data
 
        """
        if tree == None:      # recursive
           return ''
        elif tree.right== None:
           return tree.data
        else:
           return self.maxValue(tree.right)
        """

   # Prints the tree in inOrder  -- ascending order
   def inOrder(self, tree):
      if tree != None:
         self.inOrder(tree.left)
         print (tree.data, end = ' ')
         self.inOrder(tree.right)
   

   # Prints the tree in postOrder 
   def postOrder(self, tree):
      if tree != None:
         self.postOrder(tree.left)
         self.postOrder(tree.right)
         print (tree.data, end = ' ')

   
   # Prints the tree in reverseOrder  --  descending order
   def reverseOrder(self, tree):
      if tree != None:
            self.reverseOrder(tree.right)
            print (tree.data, end = ' ')
            self.reverseOrder(tree.left)

    
   # Prints the tree in preOrder 
   def preOrder(self, tree):
      if tree != None:
         print (tree.data, end = ' ')
         self.preOrder(tree.left)
         self.preOrder(tree.right)


   # Double the even values
   def dblEven(self, tree):
      .
      .
      
 
#========================================================================
        
def main():
   
   # create a tree object
   tree = BSTree()

   # add 5 nodes to BST 
   for i in range(5):
      value = random.randint(1,100)
      print ('Add value: ',value)
      tree.insert(value, tree.getRoot())
   print ()
   
   # Print the tree in inOrder
   print ('InOrder:\t', end = ' ')
   tree.inOrder(tree.getRoot())
   print ()

   # Double the even values then print the tree in inOrder
   tree.dblEven(tree.getRoot())
   print ('\nAfter double the even values:')
   print ('InOrder:\t', end = ' ')
   tree.inOrder(tree.getRoot())
   print ()

   # Print the tree in preOrder
   print ('PreOrder:\t', end = ' ')
   tree.preOrder(tree.getRoot())
   print ()
  
   # Print the tree in postOrder
   print ('PostOrder:\t', end = ' ')
   tree.postOrder(tree.getRoot())
   print ()

   # Print the tree in reverseOrder
   print ('ReverseOrder:\t', end = ' ')
   tree.reverseOrder(tree.getRoot())
   print ()
    
   # looks for a value in the tree
   value = int(input("\nEnter a value to search for: "))
   if tree.search(value, tree.getRoot()):
      print (value,'is found in the tree')
   else:
      print (value,'is not found in the tree')
   print()
   
   # Print maxValue, minValue and the size of the tree
   print ('Max value:',tree.maxValue(tree.getRoot()))
   print ('Min value:',tree.minValue(tree.getRoot()))
   print ('Size:', tree.size(tree.getRoot()))
   print ()


main()

