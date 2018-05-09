FILE_PATH = "C:\\Users\\leowk\\Desktop\\HCI computing\\H2-computing\\Text\\"
# Qn 1
'''
mode = {}
List = []

F = input("Enter name of file(.txt): ")
file = open(FILE_PATH + F,'r')
line = file.readline()
while line != '':
    line = line.rstrip()
    line.sort()
    for i in line:
        List.append(int(i))
    line = file.readline()
    
L = len(List)

if L%2 == 0: 
    first = int(L/2)
    second = first + 1           #even number
    median = (List[first]+List[second])/2
    
else:                            #odd number
    medianNo = int(L/2 + 0.5)
    median = List [(medianNo) - 1]

for i in List:
   
    if i not in mode:
        mode[i]=1

    else:
        mode[i]+=1


modeL = list(mode.values())
modeL.sort()

freq = modeL[-1]

for i in mode.keys():
    if mode[i] == freq:
        Mode =  i


print("The median is",median)
print("The mode is",Mode)
'''





#Qn 2
'''

lines = []
file = input('Enter name of file(.txt): ')


F=open(FILE_PATH + file,'r')
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
'''

#Qn 3a

uWord = []      #make a list 


F = open(FILE_PATH +'file.txt','r')        #open file and read file

line = F.readline()
while line != '':
    line = line.rstrip()
    if line not in uWord:
        uWord.append(line)
   
    line = F.readline()

uWord.sort()        #make the list in an alphabetical order
print("All the unique words are: ",uWord)        #display result

#Qn 3b
wordD = {}      #make a dictionary
F = open(FILE_PATH + 'file.txt','r')        #open file

for element in uWord:           #set all the values in dictionary to 0
        wordD[element] = 0
        
line = F.readline()     #read file

while line != '':
    line = line.rstrip()
    for keys in wordD.keys():
            if line == keys:        #update values in dictionary if key appears again
                wordD[keys]+=1
    line = F.readline()
    
for keys,values in wordD.items():
    print("The word",keys,"appeared",values,'times')        #display result

#Qn 3c
word = []       #two lists
values = []
values = list(wordD.values())
values.sort()       #select the highest value 
highestFreq = values[-1]
    
for key in wordD.keys():
    if wordD[key] == highestFreq:       #if key has a value = highest value, add it to the list:word
        word.append(key)
word.sort()        #Set the list in alphabetical order
for i in word:
    print("The most frequent word is",i)        #display result

    
    





















