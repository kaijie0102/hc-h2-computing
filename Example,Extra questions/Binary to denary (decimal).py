#!Binary to Denary
'''
def bin2Den(binary):
    sum = 0
    power = len(binary)-1
    for bit in binary:
        sum += int(bit)*(2**power)
        power = power - 1
    return sum

def main():
    for i in range(3):
        binary = input("Enter a binary number:")
        denary = bin2Den(binary)
        print('Binary:',binary)
        print('Denary:',denary)
        print()
main()         
'''

#!Denry to Binary
def Den2Bin(denary):
    
    binary=''
    quotient = denary
    while quotient != 0 :
        digit = 0
        if quotient % 2 == 1:
            digit = 1
        binary = str(digit) + binary
        quotient = quotient//2
    return binary

def main():
    for i in range(3):
        denary = int(input('Enter a positive denary:'))
        if denary == 0:
            binary = 0
        binary = Den2Bin(denary)

        print("Denary:",denary)
        print("Binary:",binary)
        print()

main()
    
        