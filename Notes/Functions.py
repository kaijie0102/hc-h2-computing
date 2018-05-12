#QN 1
'''
def calc_average(score1,score2,score3):
    Sum = score1 + score2 + score3 
    average = Sum/3
    return(average)
def determine_grade(score):
    if score >= 90 and score <=100:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    elif score>= 0 and score<60:
        grade = 'F'
    else:
        grade = "Invalid score, please enter a number from 0 to 100"

    return(grade)
'''

#QN 2(a)
def isPrime(number):
    prime = True
    for factor in range(2,number):
        if number % factor == 0:
            prime = False
    return(prime)

def partA():
    number = int(input("Enter a number: "))
    
    if isPrime(number) is True and number != 1:
        print("It is a prime number")
    else:
        print("It is not a prime number")


    
#QN 2(b)
def partB():
    print("Prime numbers: 2",end='')
    for numbers in range(3,101):
        if isPrime(numbers) == True:
            print(" ,",numbers,end='')

#QN 2(c)
def partC():
    prime = []
    for numbers in range(2,101):
        if isPrime(numbers) == True:
            prime.append(numbers)

    for elements in prime[0:20]:
        print(elements,end=' ')
        
def main():
    partC()
main()



        
