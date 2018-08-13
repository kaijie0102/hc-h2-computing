def sort(A,index_1,index_2):
    temp = A[index_1]
    A[index_1] = A[index_2]
    A[index_2] = temp
    print(A)
    
def main():
    List = [4,24,21,32,2,5,11]
    for elements in range(len(List)):
        for i in range(len(List)-1):
            if List[i] > List[i+1]:
                sort(List,i,i+1)
   
    
main()
