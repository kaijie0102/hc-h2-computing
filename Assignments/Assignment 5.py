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
