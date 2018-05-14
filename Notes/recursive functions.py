def power(x,y):
    if y == 1:
        return x
    else:
        print('n',y)
        print(x * power(x,y-1))
        return(x * power(x,y-1))
        

def main():
    x = int(input('Enter a positive integer:'))
    y = int(input('Enter a positive integer:'))
    print(x,'to the power of',y,'is',power(x,y))
main()
        