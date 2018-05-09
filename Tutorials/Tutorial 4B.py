#Qn 3
'''
Sum=0
data=[1,3,2,4,1,5]

for i in data:
    Sum += data[i]
print("Sum of all the numbers is",Sum)    
'''

#Qn 4
'''
data=[1,3,2,4,1,5]
result=[]
L = len(result)
for i in range(len(data)):
    result.insert(L,data[i])
    L = len(result)
print(result)
'''

#5
data=[-1,2,-3,4,-5]
for i in range(data):
    if data[i] < 0:
        data[i] = abs(data[i])
print(data)






