#Qn 3a

uWord = []      #make a list 


F = open('file.txt','r')        #open file and read file

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
F = open('file.txt','r')        #open file

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

    
