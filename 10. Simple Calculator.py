import os

def clear():
    os.system("CLS")

#calculator

def Add(n1,n2):
    return n1+n2

def Subtract(n1,n2):
    return n1-n2

def Multiply(n1,n2):
    return n1*n2

def Divide(n1,n2):
    return n1/n2

logo = '''

   ____      _            _       _             
  / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __ 
 | |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|
 | |__| (_| | | (__| |_| | | (_| | || (_) | |   
  \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                                

'''
print(logo)
continue_or_not = 'y'
res = 0
while continue_or_not in 'yn':
    if res == 0:
        firstNum = float(input("What is the first number: "))
    else:
        firstNum = res
    print("Operations available: + - / *")
    operation = input(f"What operation do you wanna perform?... ")
    secondNum = float(input("What is the second number: "))
    if operation == '+':
        res = Add(firstNum,secondNum)
    elif operation == '-':
        res = Subtract(firstNum,secondNum)
    elif operation == '*':
        res = Multiply(firstNum,secondNum)
    elif operation == '/':
        res = Divide(firstNum,secondNum)
    else:
        print("Operation Unavailable")
    print("Result:", res)
    continue_or_not = input("Enter y to continue calculating or n to reset the calculator to 0...")
    
    if continue_or_not == 'n':
        res = 0
        clear()
        print(logo)
    

