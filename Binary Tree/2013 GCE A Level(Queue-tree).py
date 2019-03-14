#Task 3.1
class Node:
    def __init__(self,Left = 0):
        self.LeftP = Left
        self.data = ""
        self.RightP = 0

class Tree:
    def __init__(self):

        self.ThisTree = [None]*21

        #set up empty tree
        self.Root = 0
        self.NextFreePosition = 1

        for i in range(1,19+1):
            self.ThisTree[i] = Node(i+1)

        self.ThisTree[20] = Node(0) #last node with pointer 0
    #Task 3.3
    def OutputData(self):
        print("Root: ",self.Root)
        print("NextFreePosition: ", self.NextFreePosition)
        print("%10s%10s%10s%10s"%('index','left','data','right'))
        for i in range(1,20+1):
            print("%10s%10s%10s%10s"%(str(i),str(self.ThisTree[i].LeftP),str(self.ThisTree[i].data),str(self.ThisTree[i].RightP)))
        return self.ThisTree
    
    #Task 3.2
    def AddItemToBinaryTree(self,item):
        if self.NextFreePosition == 0:
            print("The tree is full!")
        else:
            #get next free node and update NextFreePosition
            NewNodePos = self.NextFreePosition
            self.NextFreePosition = self.ThisTree[self.NextFreePosition].LeftP

            #inserting data, making pointers 0 as new node is the leaf node
            self.ThisTree[NewNodePos].data = item
            self.ThisTree[NewNodePos].LeftP = 0
            self.ThisTree[NewNodePos].RightP = 0

        #perform insertion
        LastMove = ''
        if self.Root == 0:
            self.Root = NewNodePos
        else:
            CurPos = self.Root      #start from root

            while CurPos != 0:
                PrevPos = CurPos
                if item < self.ThisTree[CurPos].data:
                    LastMove = 'L'
                    CurPos = self.ThisTree[CurPos].LeftP
                else:
                    LastMove = 'R'
                    CurPos = self.ThisTree[CurPos].RightP

            if LastMove == "L":
                self.ThisTree[PrevPos].LeftP = NewNodePos
            else:
                self.ThisTree[PrevPos].RightP = NewNodePos
        return (item, 'has been added!')

    #***************memorise ********************
    #Task 3.6
    def InOrderTraversal(self,index):
        if index != 0:
            self.InOrderTraversal(self.ThisTree[index].LeftP)
            print(self.ThisTree[index].data,end= ' ')
            self.InOrderTraversal(self.ThisTree[index].RightP)
            
    def getRoot(self):
        return self.Root
    
#Tsak 3.4                
def main():
    tree = Tree()
    print()
    print('EmptyTree:\n==========')
    tree.OutputData()
    print()
    print('Non-EmptyTree:\n=============')
    inp = input("Enter data item (XXX to end): ")
    while inp != 'XXX':
        tree.AddItemToBinaryTree(inp)
        inp = input("Enter data item (XXX to end): ")

    print()
    
    tree.OutputData()
    root = tree.getRoot()
    print(tree.InOrderTraversal(root))
main()
