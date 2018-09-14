#!Put one element into the correct postion. Repeat for elements in smaller sublist
#*Pivot will be the partition to two smaller sub lists
def swap(List,a,b):
    temp = List[a]
    List[a] = List[b]   
    List[b] = temp

def QuickSort(List,x,y):
    if x>=y:
        return  
    pivot = List[x]
    borderIndex = x+1
    border = List[borderIndex]
    pointerIndex=x+1
    
    while pointerIndex <= y:
        pointer = List[pointerIndex]
        if pointer<pivot:
            swap(List,borderIndex,pointerIndex)
            borderIndex += 1
            border=List[borderIndex]
        pointerIndex += 1
        
    swap(List,x,borderIndex-1)               #!borderIndex is 1 above the 'real' index                                                                                        
    QuickSort(List,x,borderIndex-2)
    QuickSort(List,borderIndex,y)

def main():
    List = [21,41,12,45,2,8,10,39,88]
    QuickSort(List,0,len(List)-1)
    print(List)
main()