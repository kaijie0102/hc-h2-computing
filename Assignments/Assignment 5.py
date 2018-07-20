#!QN 1
'''
def multiplication(x,y):
    if y>0:
        return x + multiplication(x,y-1)
    else:
        return 0
    
def main():
    x = int(input('Enter value of x'))
    y = int(input('Enter value of y'))
    print(multiplication(x,y))
main()
'''

#!QN 2
def asterisk(n,count=1):
   
    if count>n:
        return None
    else:
        print(count*'*')
        return asterisk(n,count+1)

asterisk(4)