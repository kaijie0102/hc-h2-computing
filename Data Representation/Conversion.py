def bin2dec(binary):
    decimal = 0
    count=0
    for bit in range(len(binary)-1,-1,-1):
        decimal += int(binary[bit]) * (2**count)
        count+=1
    return decimal

def dec2bin(decimal):
    binary = ''
    while decimal != 0:
        remainder = decimal%2
        decimal = decimal//2
        binary = str(remainder) + binary
    return binary

def oct2dec(octal):
    decimal = 0
    count=0
    for x in range(len(octal)-1,-1,-1):
        decimal += int(octal[x]) * (8**count)
        count+=1
    return decimal

def dec2oct(decimal):
    octal = ''
    while decimal != 0:
        remainder = decimal%8
        decimal = decimal//8
        octal = str(remainder) + octal
    return octal


def hex2dec(hexadecimal):
    decimal = 0
    count=0
    for x in range(len(hexadecimal)-1,-1,-1):
        if hexadecimal[x] == 'A':
            x=10
        elif hexadecimal[x] == 'B':
            x=11
        elif hexadecimal[x] == 'C':
            x=12
        elif hexadecimal[x] == 'D':
            x=13 
        elif hexadecimal[x] == 'E':
            x=14
        elif hexadecimal[x] == 'F':
            x=15
        print(x)
        if x>9:
            decimal += x * (16**count)
            count+=1
        else:
            decimal += int(hexadecimal[x]) * (16**count)
            count += 1
    return decimal

def dec2hex(decimal):
    hex = ''
    while decimal != 0:
        remainder = decimal%16
        decimal = decimal//16
        if remainder == 10:
            remainder = 'A'
        elif remainder == 11:
            remainder = 'B'
        elif remainder == 12:
            remainder = 'C'
        elif remainder == 13:
            remainder = 'D'
        elif remainder == 14:
            remainder = 'E'
        elif remainder == 15:
            remainder = 'F'        
        hex = str(remainder) + hex
    return hex

def main():
    #a=bin2dec('101001011')
    #a=dec2oct(331)
    #a = oct2dec('513')
    a=dec2hex(331)
    
    print(a)
main()