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

