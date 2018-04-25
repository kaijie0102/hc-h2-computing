#QN 1
N = int(input("Enter the integer:"))
number = 1
fac = 1
while(number<=N):
        fac = fac * number
        number += 1
print(fac)


#QN 2
A = float(input("Enter the number:"))
while A < 0:
    print("ERROR:Number must be positive")
    A = float(input("Enter the number:"))

epsilon = 0.00001

x = 1

while abs(x-A/x)>epsilon:
    ave = (x+A/x)/2
    x = ave
    

print("The square root of ",A,"is %.2f"%ave)
    


#QN 3
num = 0
name = input("Enter item name or enter 'xyz' to stop:")
while name != 'xyz':
    
    price = float(input("Enter the price per item:"))
    quantity = int(input("Number of items bought:"))
    total= quantity * price
    print('%1d %-10s $%.2f'%(quantity,name,total))
    num = num + total
    
    name = input("Enter item name or enter 'xyz' to stop:")

print("Total bill is $%.2f"%num)
