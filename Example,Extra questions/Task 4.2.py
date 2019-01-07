#Task 4.2
import random

def Random():
    x = random.randint(1,8) -  1
    y = random.randint(1,15) - 1 
    return (x,y)

def fish(pond,x,y):
    pond[x][y] = 'F'

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
    
    for i in range(3):
        x,y = Random()
        fish(pond,x,y)
    displayGrid(pond,length,breadth)

main()

