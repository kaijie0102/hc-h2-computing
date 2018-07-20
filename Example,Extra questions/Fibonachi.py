def fib(n):
    if n <= 3:
        return n
    else : 
        return fib(n-1)+fib(n-2)+fib(n-3)
def main():
    print('The first 8 numbers in the sequence:') 
    for i in range(1,9):
        print(fib(i),end=' ')     
main()