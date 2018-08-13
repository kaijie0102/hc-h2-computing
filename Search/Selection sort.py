def sort(List,first,second):
    temp = List[first]
    List[first]= List[second]
    List[second]= temp
    print(List)

def main():
    List = input("Enter a list: ")
    List = [63,3,2,44,1,4,22,12,52,23]
    

    for i in range(len(List)-1):
        low = List[i]

        for num in range(i+1,len(List)):
            if List[num] < low:
                low = List[num]
                low_index = num 
                
            if num == len(List)-1 and List[i]>low:
                sort(List,i,low_index)

main()


