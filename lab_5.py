'''5. Write a program to create a menu with the following options
1. TO PERFORM ADDITITON
2. TO PERFORM SUBTRACTION
3. TO PERFORM MULTIPICATION
4. TO PERFORM DIVISION
Accepts users input and perform the operation accordingly. Use functions with arguments.'''

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul (a,b):
    return a*b
def div(a,b):
    return a/b


print("Enter two numbers ")
a=int(input())
b=int(input())
print("choose from below list\n 1.addition\n2.subtraction\n3.multiplication\n 4.division\n>>> ")
choose=int(input())
if choose==1:
    print("The addition is:",add(a,b))

if choose==2:
    print("The subtraction is:",sub(a,b))

if choose==3:
    print("The multiplication is:",mul(a,b))

if choose==4:
    print("The division is:",div(a,b))




