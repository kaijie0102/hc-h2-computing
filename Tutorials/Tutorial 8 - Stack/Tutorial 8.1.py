#Qn 2
'''
"""
File: brackets.py
Checks expressions for matching brackets
"""

from stack import ArrayStack

def bracketsBalance(exp,Open,Close):          
    """exp represents the expression"""
    stk = ArrayStack()                      # Create a new stack
    for ch in exp:                   # Scan across the expression
        if ch in Open:           # Push an opening bracket 
            stk.push(ch)
        elif ch in Close:         # Process a closing bracket
            if stk.isEmpty():               # Not balanced
                return False                  
            chFromStack = stk.pop()
            # Brackets must be of same type and match up
            
            OpenIndex = Open.index(chFromStack)
            CloseIndex = Close.index(ch)
            
            if OpenIndex != CloseIndex:
                return False
    
    return stk.isEmpty()                   # They all matched up


def main():
    exp = input("Enter a bracketed expression: ")   
    if bracketsBalance(exp,['[','(','{'],[']',')','}']):
        print ("OK")
    else:
        print ("Not OK")

main()
'''

#Qn 3
'''
from stack import ArrayStack
def isPalin(exp):
    revStr = ''
    stk = ArrayStack()
    for ch in exp:
        stk.push(ch)
    while not stk.isEmpty():
        revStr = revStr + stk.pop()

    if revStr == exp:
        return True

    else:
        return False

def main():
    word = 'rats live on no evil star'
    print(isPalin(word))

main()
'''

#Qn 4
'''
from stack import ArrayStack
def selectItem(s,n):
    stk2 = ArrayStack()
    found = False

    while not s.isEmpty() and not found:
        if s.peek() == n:
            s.pop()
            found = True

        else:
            stk2.push(s.pop())

    if s.isEmpty() and not found:
        print('Item not found')
        return
    
    while not stk2.isEmpty():
        s.push(stk2.pop())
      
    s.push(n)
    print(s.__str__())                 
        


def main():
    stk = ArrayStack()
    num = '1234567890'
    for Int in num:
        stk.push(int(Int))
    selectItem(stk,5)
main()
'''

#Qn 5
from stack import ArrayStack
def multiBaseOutput(num,b):
    stk = ArrayStack()
    s1 = ''
    
    while num != 0:
        stk.push(str(num%b))
        num = num//b
        
    while not stk.isEmpty():
        s1 += stk.pop()

    return s1

def main():
    num = int(input("Enter a number: "))
    b = int(input("Enter a integer (2-9): "))
    print(multiBaseOutput(num,b))
    
main()



























