#*Set one element(pivot) into correct position and that will serve as a partition between two sub-lists, repeat
def swap(List,a,b):     #*Swap two numbers
    temp = List[a]
    List[a] = List[b]
    List[b] = temp

def QuickSort(List):
    #print('L',List)

    if len(List) <= 1:      #*Stop breaking into smaller sublists when element is <=1
        return List

    else:
        pivot = List[0]
        left = 1
        right = len(List)-1
        #print(List)
        while left < len(List)-1 and List[left] <= pivot: 
            left += 1       #*Select first number
        while List[right] > pivot:
            right -= 1      #*Select second number
        
        if left < right:        #*Swap first and second number if the pointers have not crossed each other
            swap(List,left,right)
            return QuickSort(List)  #*Select another two number

        else:       #*Two pointers have crossed each other
            swap(List,right,0)
            #!print('a',List,right)
            return QuickSort(List[:right]) + [List[right]] + QuickSort(List[right+1:])  #*Break into smaller lists

def main():
    List = [12,14,44,24,5,35,96,1]
    print(QuickSort(List))

main()