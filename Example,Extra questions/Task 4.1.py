#Task 4.1
def throwStone(pond,x,y):
    pond[x][y] = 'S'

def displayGrid(pond,length,breadth):
    for i in range(breadth):
        for j in range(length):
            print(pond[i][j],end='')
        print('\n')

def main():
    length = 15
    breadth = 8
    
    print("1,1 is top left")
    y = int(input('Enter X-coordinate<1-15>: '))
    x = int(input('Enter Y-coordinate<1-8>: '))
    
    
    x-=1
    y-=1
    pond = []
    for i in range(breadth):
            pond.append(['.']*length)
    print(pond)
    throwStone(pond,x,y)
    
    displayGrid(pond,length,breadth)

main()



    

    