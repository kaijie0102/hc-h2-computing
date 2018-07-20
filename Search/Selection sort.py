def sort(list,first,second):
    x = list[first]
    list[first]=list[second]
    list[second]=list[first]
sort([1,2,3],0,2)
print(list)