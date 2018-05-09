#!QN 1
'''
numL = []

Sum = 0

number = input('Enter a series of number: ')

for i in number:
    numL.append(int(i))
    
for i in numL:
    Sum += i  
    
number = len(numL)
ave = Sum/number
numL.sort()
largest = numL[-1]


print("The sum is",Sum)    
print("Average of digits is",ave)
print("Largest digit is",largest)
'''

#!QN 2
'''
count = 0
choice = input("Choice? 1.EXACT 2.START 3.WITHIN - ")
term = input("Term? - ")

if choice == '1':
    F = open('jargon.txt','r')
    line = F.readline()
    while line!='':
        line = line.rstrip()
        if line == term:
            count += 1
        line = F.readline()       
        
    print("There were",count,"matching term(s)")

if choice == '2':
    lterm = len(term)
    list = []
    F = open('jargon.txt','r')
    line = F.readline()
    
    while line!='':
        
        line = line.rstrip()
        list.append(line)
       
        line = F.readline()
    for i in list:
        if term == i[0:lterm]:          #alt methods
            count+=1    
        
        #alt method 
        if i.startswith(term):              
        
        
    print("There were",count,"matching term(s)")

if choice == '3':
    F = open('jargon.txt','r')
    line = F.readline()
    while line != '':
        line = line.rstrip()
        #
        print(line)
        if term in line:
            count+=1
        line = F.readline()
       
    print("There were",count,"matching term(s)")
'''            
    
#!QN 3
'''
FILE_PATH = "C:\\Users\\leowk\\Desktop\\HCI computing\\H2-computing\\Text\\"

length = []
nameDate = {}
names = []
F = open('weblog.txt','r')
for lines in F:
    lines = lines.rstrip()
    name,details = lines.split(' - - ')
    
    date = details[1:12]
    if name not in nameDate:
        nameDate[name] = [date]
    else:
        nameDate[name].append(date)
        
for elements in nameDate.values():
    length.append(len(elements))
length.sort()
maxFreq = length[-1]

for keys,value in nameDate.items():
    if len(value) == maxFreq:
        names.append(keys)
        

        
F1 = open('summary.txt','w')
for keys,values in nameDate.items():
    F1.write('%-30s'%keys)
    for number in range(len(values)):
        if number == len(values)-1:
            F1.write(values[number]+'\n')
        else:
            F1.write(values[number]+',')
                     
print('Highest frequency is',maxFreq)
print('Accessed by: ')
for i in names:
    print(i)
F1.close()
'''

#!QN 4
def random():
    import random
    ranNum = random.randint(1,50)
    #
    print(ranNum)
    
    tries = 0
    success = False
    number = int(input('Guess a number from 1 to 50: '))
    
    while tries <= 6 and success == False:
        if number == ranNum:
            print('Congratulations!')
            success = True
            tries += 1
            #
            print(success,tries)
        elif number < ranNum:
            print('Too low')
            tries += 1
            number = int(input('Guess a number from 1 to 50: '))
        elif number > ranNum:
            print('Too high')
            tries += 1
            number = int(input('Guess a number from 1 to 50: '))
    if tries == 7:
        print('Sorry, you did not get it right. The answer is',ranNum)   

def main():
    game = {}
    fail = 0

    for games in range(1,11):
        random()
        if random() is False:
            fail += 1
        else:
            for num in range (1,7):
                game[num] = 0
                if tries == num:
                    game[num] += 1
            




    print('%-10s%-10s'%('NumGuess','NumGames'))
    
    for numb in range (1,7):
        print('%-10d'%num)

    keys , values = game.items()
    keys.sort()
    for key in keys:
        print('%-10d'%game[key])


    print('Unsuccessful games: ',fail)
    
main()































