#Task 4.2
import random

def Random():
    x = random.randint(1,8) -  1
    y = random.randint(1,15) - 1 
    return (x,y)

def fish(pond,x,y):
    pond[x][y] = 'F'

def pellet(pond,x,y):
    pond[x][y] = 'P'

def happy_fish(pond,x,y):
    pond[x][y] = 'H'

def displayGrid(pond,length,breadth):
    for i in range(breadth):
        for j in range(length):
            print(pond[i][j],end='')
        print('\n')

def main():
    length = 15
    breadth = 8
    
    pond = []
    for i in range(breadth):
            pond.append(['.']*length)
    
    x,y = Random()
    x1,y1 = Random()
    
    if (x,y) == (x1,y1):
        happy_fish(pond,x,y)
    
    else:
        fish(pond,x,y)
        pellet(pond,x1,y1)

    displayGrid(pond,length,breadth)

main()

