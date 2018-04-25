#QN 1
'''
s = 'myString'
for char in range(-1,-len(s)-1,-1):
    print(s[char],end='')
'''

#QN 2
#method 1:
'''
myString='qiuweihong'
reversedString=''
for char in range(-1,-len(myString)-1,-1):
    reversedString += myString[char]

print('reversedString=',reversedString)
'''
#method 2:
'''
myString='abcd'
reversedString= ''
for char in myString:
    reversedString = char+reversedString
print('reversed string is',reversedstring)
'''
    

#QN 3
'''
file1 = input('Enter name of file to copy from (.txt) : ')
file2 = input('Enter name of file to copy to(.txt): ')

F = open(file1,'r')
content=F.read()
F.close()



F2 = open(file2,'w')
F2.write(content)
F2.close()
'''

#QN 4 Mtd 1
'''
file1=input('Enter name of file 1 (.txt) : ')
file2=input('Enter name of file 2 (.txt) : ')

F1=open(file1,'r')
F2=open(file2,'r')


line1=F1.readline()
line2=F2.readline()
while line1 == line2 and line1 !='' and line2 != '':
    line1=F1.readline()
    line2=F2.readline()
if line1 != line2:
    print('No')
    line1 = line1.rstrip()
    line2 = line2.rstrip()
    print(line1,line2)
else:
    line1=F1.readline()
    line2=F2.readline()
    

F2.close()
F1.close()
'''
#QN 4 Mtd 2
'''
file1=input("Enter the 1st file to open:")
file2=input("Enter the 2nd file to open:")

finished = False

F1 = open(file1,'r')
F2 = open(file2,'r')

while not finished:
    line1 = F1.readline().rstrip()
    line2 = F2.readline().rstrip()

    if line1 == line2:
        if line1 == '':
            print('YES')
            finished = True

    else:
        print('NO')
        if line1 == '':
            line2=line2
            print('file 1 has ended')
            print(line2)
        elif line2 == '':
            line1 = line1
            print(line1)
            print('file 2 has ended')
        else:
            print(line1,line2)
        finished = True
'''        
        
            
        



#QN 5
file=input('Enter the file name: ')     #request for file name

F=open(file,'r')        #open file

print('%-15s%-17s%-15s'%('<last name>','<hourly wage>','<hours worked>'))       #print heading

line = F.readline()     #read file
while line != '':
    line = line.split('|')      #remove all |
    name=line[0]        #assign variables
    wage=line[1]
    hours=line[2]
    line = F.readline()
    print('%-15s%-18.1f%-8d'%(name,float(wage),int(hours)))     #print data on shell



F.close()
