def seqSearch(A, start, n , key):
    print(A,start,n,key)
    #search the n-element interger array A for match with key from start position
    #return index of key of -1 if key not found
    #search from start to end
    i = start - 1
    found = False

    while found == False and i < n:
        
        if A[i] != key:
            i += 1
            
        else:
            found = True
            return i
    
    if found == False:
        return -1
def main():
    number = input("Enter a list of number: ")
    noNum = int(input("How many numbers are there?"))
    List = []
    for i in range(1,noNum+1):
        List.append(number[i-1])
    
    start = int(input("Enter start position: "))
    key = input("Enter the thing you want to find: ")
    if seqSearch(List,start,len(List),key) == -1 :
        print("There is no such number.")
    else:
        print("The number is in the index",seqSearch(List,start,len(List),key),'.')
       
       
main()
