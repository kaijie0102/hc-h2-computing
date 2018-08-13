def swap(List,a,b):
    temp = List[a]
    List[a] = List[b]
    List[b] = temp

def main():
    List = [21,41,12,45,2,8,10,39,88]
    print(List)
    pivotCount=0
    stop = False 
    while stop != True:
        pivotCount+=1
        pivot = 0
        border = 1

        for pointer in range(2,len(List)):
            if List[pointer] < List[pivot]:
                swap(List,border,pointer)
                border += 1
        swap(List,pivot,border)

        if pivotCount == len(List):
            stop = True
        print(List)
main()


