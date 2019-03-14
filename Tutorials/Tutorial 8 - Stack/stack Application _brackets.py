"""
File: brackets.py
Checks expressions for matching brackets
"""

from stack_array import Stack
#from stack_linked import Stack


def bracketsBalance(exp):          
    """exp represents the expression"""
    stk = Stack()                      # Create a new stack
    for ch in exp:                     # Scan across the expression
        if ch in ['[', '(', '{']:      # Push an opening bracket 
            stk.push(ch)
        elif ch in [']', ')', '}']:    # Process a closing bracket
            if stk.isEmpty():          # Not balanced
                return False                  
            chFromStack = stk.pop()
            # Brackets must be of same type and match up
            if (ch == ']' and chFromStack != '[') or \
               (ch == '}' and chFromStack != '{') or \
               (ch == ')' and chFromStack != '(') :
                return False
    return stk.isEmpty()               # They all matched up


def main():
    exp = input("Enter a bracketed expression: ")
    if bracketsBalance(exp):
        print ("OK")
    else:
        print ("Not OK")

main()
