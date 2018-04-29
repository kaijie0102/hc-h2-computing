#Qn 3
'''
Sum=0
data=[1,3,2,4,1,5]
l=len(data)
for i in range(l):
    Sum += data[i]
print("sum of all the numbers is",Sum)    
'''

#Qn 4
data=[1,3,2,4,1,5]
result=[]
L = len(result)
for i in range(len(data)):
    result.insert(L,data[i])
    L = len(result)
print(result)
