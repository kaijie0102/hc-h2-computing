#QN 2
for name in range(50):
    print('Leow Kai Jie')


#QN 3
number = 0
for i in range(1,129):
    print(number,chr(number))
    number = number + 1


#QN 4
testString = input('string:')
for character in testString:
    print(character,ord(character))


#QN 5
space = 0
string = input('String:')
for word in string:
    if ord(word) == 32:
        space +=1
    
print('The total number of spaces are',space)


#QN 6
pi4 = 0
number = int(input('Enter iterations:'))
for p in range(number+1):
    pi4 = (pi4) + ((-1)**p / (2 * p + 1))
pi = pi4 * 4
print(pi)


#QN 7
count = 0
total = 0
for i in range(1,8):
    temp = float(input("Temperature of the day " + str(i) + ':'))
    if temp > 0:
        total+=temp
        count+=1
aveTemp = total/count
print('The average temperature is',aveTemp)


#QN 8
n = int(input('Total number of integers:'))

total = 0
for integer in range(1,n+1):
    sq = integer ** 2
    total += sq
print('The sum of all the squared values is',total)


#QN 9
print('%-13s%-6s'%('Length','Area'))
for x in range(10,46):
    area = x * (100 - 2*x)/2
    print('%4d%12d'%(x,area))
print('The maximum area is 625 units sq')


#QN 10
print('%-7s%-6s'%('PRICE','PROFIT'))
for p in range(10,31):
    profit = p * (100-3*p)
    print('%5d%8d'%(p,profit))


#QN 11
col = int(input('Number of columns:'))

print('    ',end='')
for r in range(1,col+1):
    print('%-4d'%r,end='')
print()
for c in range(1,col+1):
    print('%-4d'%c,end='')
    for x in range (1,c+1):
        print('%-4d'%(x*c),end='')
    
    print()




    
