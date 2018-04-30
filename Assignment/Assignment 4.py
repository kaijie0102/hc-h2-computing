#Qn 1
F = 
List = []
l = len(List)
if l%2 == 0:
    


#Qn 2
lines = []
file = input('Enter name of file(.txt): ')


F=open(file,'r')
line = F.readline()
while line!='':
    line = line.rstrip()
    lines.append(line)
    line = F.readline()
number = len(lines)
print('The total number of lines in the file is',number)

lineNo = int(input('Enter a line number or 0 to quit: '))

while lineNo != 0:
    if lineNo > number or lineNo < 0:
        print('Invalid line number !')
        lineNo = int(input('Enter a line number or 0 to quit: '))
        print()
    else:
        print('Line',lineNo,':',lines[lineNo - 1])
        lineNo = 0
