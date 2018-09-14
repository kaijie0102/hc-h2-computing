def sort(List,first,second):
    temp = List[first]
    List[first]= List[second]
    List[second]= temp
    print(List)

def main():
    List = input("Enter a list: ")
    List = [63,3,2,44,1,4,22,12,52,23]
    

    for i in range(len(List)-1):        #*Don't need to compare last number/Nothing to compare
        low = List[i]

        for num in range(i+1,len(List)):    #*Check if 
            if List[num] < low:
                low = List[num]
                low_index = num 
                
            if num == len(List)-1 and List[i]>low:      #*Check if num is at end of array and that List[i] isnt the smalles
                sort(List,i,low_index)      #* Swapping SMALLEST number in list to the front

main()


