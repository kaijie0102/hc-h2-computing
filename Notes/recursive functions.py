'''
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


total=0
def Sum(lower,upper):
    if lower <= upper:
        return lower + Sum(lower+1,upper)
    
    else:
        return 0
'''       
'''
def main():
    first = int(input('Enter the first integer: '))
    
    second = int(input('Enter the second integer: '))

    print('The sum of the numbers from',first,'to',second,'is',Sum(first,second))
main()       
'''
        