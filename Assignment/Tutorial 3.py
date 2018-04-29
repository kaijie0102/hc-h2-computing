#QN 1a
s1 = 'abc'
s2 = '1234'
s1 = ''

for char in range(0,len(s2)-1+1):
    s1 = s1 + s2[char]

print('s1:',s1)
print('s2:',s2)


#QN 6
F = open('myfile.txt','w')

F.write('abc.\nadasdasdasd.\nasdadsada.\n')

F.close()

NoLine = 0
F = open('myfile.txt','r+')
line = F.readline()
while line != '':
    line = F.readline()
    NoLine += 1
F.write('The number of lines is ')
F.write(str(NoLine))

F.close()   


#QN 7
F = open('hello.txt','w')
F.write('asda\n asdd\n dsddashgugguu\n asda\n asda\n asda\nabcdefghiijk\n')
F.close()


F=open('hello.txt','r+')
lines = F.readlines()

word = 0

for words in lines:
        
        if len(words.strip()) == 4:
            word += 1
        lines = F.readline()   
    
    
    
            
F.write('The number of 4 letter words is ')

F.write(str(word))

F.close()
print(word)


#QN 8
F = open('kjfiles.txt','w')
F.write('100\n000\n0000\n')
F.close()

F = open('kjfiles.txt','r+')
number=0
total=0
line=F.readlines()
for numb in line:
    number+=1
    total=total+int(numb)
  
   


average=total/number

F.write('The average is ')
F.write(str(average))

        
F.close()
print(average)


