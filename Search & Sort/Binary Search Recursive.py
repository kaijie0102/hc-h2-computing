def binSearch(A,n,key,low=0,high=-1):   #A is list, n is len of list,key is item to find
    
    if high == -1:      #first time 
        high = n-1
        
        
    mid = (high+low)//2  #looking for index of the middle number low + (high-low)//2
    if A[mid] == key:
        return mid
    
    if low == high :        #Object not in array, after checking that the last number is not key
        return -1
             
    if A[mid] > key:
        return binSearch(A,n,key,low,mid-1)     #Sublist 
    
    elif A[mid] < key:
        #print(mid+1,high)
        return binSearch(A,n,key,mid+1,high)        #breaking into sublist
                                                                   
                           
def main():
    print("Enter a list of 7 integers in order")
    #A = [1,2,3,4,5,7,8]
    
    for i in range(7):      #making a list
        num = input("Enter an integer: ")
        A.append(num)
    print('A=',A)
    

    pos = 0
    n=len(A)
    
    key = input("Enter a key: ")
    pos = binSearch(A,n,int(key))
    if(pos != -1):
        print("The key is in the position", pos+1)
    else:
        print("The number is not found")
main()
