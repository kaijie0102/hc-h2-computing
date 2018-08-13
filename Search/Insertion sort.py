def sort(A,index_1,index_2):
    temp = A[index_1]
    A[index_1] = A[index_2]
    A[index_2] = temp
    print(A)

def main():
    List = [12,42,23,4,39,25,69,1]
    for element in range(1,len(List)):
        if List[element]<List[element-1]:
            for i in range(element,0,-1):
                if List[i]<List[i-1]:
                    sort(List,i,i-1)
main()
        
def bin(a,max,min):
    mid = (max+min)//2
    
