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
      self.Root = None
      
   # Adds new node   
   def insert(self, newValue, tree):    # recursive
      if tree == None:
         self.Root = TreeNode(newValue)
      elif(newValue > tree.data):
         if tree.right == None:
            tree.right = TreeNode(newValue)
         else:
            return self.insert(newValue, tree.right)
      else:
         if tree.left == None:
            tree.left = TreeNode(newValue)
         else:
            return self.insert(newValue, tree.left)
      

  
   # Looks for a value in the tree   
   # Returns False if not found else returns True
   def search(self, target, tree):      # recursive
      if tree == None:
         return False

      if target == tree.data:
         return True
      elif (target > tree.data):
         return self.search(target, tree.right)
      else:
         return self.search(target, tree.left)
                            
      

 
   # Gets the root of the tree
   def getRoot(self):
      return self.Root


   # Gets the size of the tree, i.e. number of nodes
   def size(self, tree):
      if tree == None:
         return 0
      else:
         return self.size(tree.left) + 1 + self.size(tree.right)


   # Gets the minimum value
   def minValue(self, tree):
      # goes down into the left arm and returns the last value
      
      if tree == None:
         return ''
      elif tree.left == None:
         return tree.data
      else:
         return self.minValue(tree.left)  #recursive
      '''
      #Non-recursive
      if tree == None:
         return''
      else:
         while tree.left != None:
            tree = tree.left

         return tree.data
      '''     

   
   # Gets the maximum value
   def maxValue(self, tree):
        # goes down into the right arm and returns the last value
      if tree == None:
         return ''
      elif tree.right == None:
         return tree.data
      else:
         return self.maxValue(tree.right)  #recursive


   # Prints the tree in inOrder  -- ascending order
   def inOrder(self, tree):
      if tree != None:
         self.inOrder(tree.left)
         print(tree.data, end =' ')
         self.inOrder(tree.right)
      
   

   # Prints the tree in postOrder(left, right, root)
   def postOrder(self, tree):
      if tree != None:
         self.postOrder(tree.left)
         self.postOrder(tree.right)
         print(tree.data, end =' ')
      
   # Prints the tree in reverseOrder  --  descending order
   def reverseOrder(self, tree):
      if tree != None:
         self.reverseOrder(tree.right)
         print(tree.data, end =' ')
         self.reverseOrder(tree.left)
        
   # Prints the tree in preOrder 
   def preOrder(self, tree): #(root,left,right)
      if tree != None:
         print(tree.data, end =' ')
         self.preOrder(tree.left)
         self.preOrder(tree.right)
    
  
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

