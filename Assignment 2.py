#QN 1
S1 = float(input('Enter length of side 1: '))
S2 = float(input('Enter length of side 2: '))
S3 = float(input('Enter length of side 3: '))

if S1<0 or S2<0 or S3<0:
    print('Error:Lengths must be positive.')
else:
    if S1 == S2 == S3:
        print('The triangle is an equilateral triangle')
    else:
        print('The triangle is not an equilateral triangle')
    

#QN 2
vowel = 0
letter = 0
word = input('Enter the word: ')
for w in word:
    letter += 1
    if w in 'aeiouAEIOU':
        vowel += 1
pct = vowel/letter * 100
print('Letters:',letter)
print('Vowels:',vowel)
print('Percentage of vowels:%.2f'%pct+'%')

#QN 4
n = int(input('Enter number: '))
for c in range (1,n+1):
    if c == 1 or c == n:
        print(2*n*'*')
    else:
        print('*' + (2*n-2)*' ' + '*')

#QN 5
GCD = 0
A = int(input('Enter value of A: '))
B = int(input('Enter value of B: '))

if A > B:
    while B > 0:
        remainder = A%B
        A=B
        B=remainder
    GCD = A
else:
    while A > 0:
        remainder = B%A
        B=A
        A=remainder
    GCD = B
print('The GCD is',GCD)

#QN 6
Sum = 0
Max = 0
numb = 0
for number in range(100,111):
    print(number,': ',end='')
    for div in range (1,number+1):
        if number%div == 0:
            Sum = Sum + div
            print(div,end='  ')
        
            
            if Sum > Max:
                Max = Sum
                numb = number
    print('')
    print('sum of divisors is',Sum)           
    Sum = 0
            
    
    print()

print(numb,'has the maximum sum of divisors')
            

#QN 6
max=0

for number in range(100,111):
    total = 0
    print(number,':',end=' ')
    for num in range(1,number+1):
        remainder = number % num
        if remainder == 0:
            print(num,' ',end='')
            total = total + num
        if total>max:
            max=total
            maxNo=number
        
    print()
    print('sum of divisors',total)

print()    
print(maxNo,'has the maximum sum of divisors')
print()
            
    

#QN 8
import random

#initialise constant
count = 0
max=0

#request for input
money=int(input('Enter the amount of money you wish to start with ($):'))

while money > 0:
    count+=1
    roll=random.randint(1,6)
    roll2=random.randint(1,6)
    if roll + roll2 == 7:
        money=money+4
    else:
        money=money-1
        if money > max:
            max = money

#display results
print('The number of rolls it took to break the player is',count)
print('The maximum amount of money in the pot is $',max)


#QN 9A
import random
number=random.randint(1,100)
tries = 1
guess=input('Enter your guess:')
while guess != number:
    tries+=1
    guess=input('Enter your guess:')
    if guess > number:
        print('Too large')
    if guess < number:
        print('Too small')
print('You got in in',tries,'tries')


#QN 9B
tries = 1
import random
guess = random.randint(1,100)
number = int(input('Enter the number you are thinking of:'))

while guess!=number:
    tries+=1
    guess = random.randint(1,100)
print('The computer has guessed your number after',tries,'trie(s)')

#QN 10
#initialise the constants
ace = 0
Pass = 0
student = 0

#request for inputs
name = input('Enter name of student or enter X to stop:')   
while name != 'X':
    
    grade1 = int(input('Enter grade of first subject:'))
    grade2 = int(input('Enter grade of second subject:'))
    grade3 = int(input('Enter grade of third subject:'))
   
    ave = (grade1 + grade2 + grade3)/3
    print('Your average grade is',ave)
    
    if ave >= 80:
        ace += 1
        Pass += 1
        print('Congratulations! You aced the test!')
        
    elif ave>=60:
        print('Congratulations! You passed the test!')
        Pass += 1
    else:
        print('You have failed the test,try harder next time')
    print()
    name = input('Enter name of student or enter X to stop:')
    
print('The total number of students who passed is',Pass)
print('The total number of students who scored 80 and above is',ace)
   
    



