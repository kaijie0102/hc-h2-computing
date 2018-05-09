#QN 1
#initialise the constants
stdDeduct = 10000
dpDeduct = 2000
rate = 0.2

#request the inputs
grossInc = float(input('Enter your gross income ($):'))
dependents = int(input('Enter number of dependents:'))

#compute total income tax
taxInc = grossInc - stdDeduct - dpDeduct * dependents
incTax = taxInc * rate

#display total income tax
print()
print('Your total income tax is $%0.2f'%(incTax))


#QN 2
name = input('Name:')
age = int(input('Age:'))
age10 = age + 10
print()
print('Age in 10 years will be', age10)

#QN 3
import math
math.pi

pi = dir('pi')
rad = float(input('Radius:'))

diameter = 2 * rad
circ = diameter * pi 


#!QN 4
base = float(input('Base of triangle:'))
height = float(input('Height of triangle'))
area = base * height
print()
print('The area of the triangle is %.2f unit sq'%(area))

