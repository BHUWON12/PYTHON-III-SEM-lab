'''10. Write a program to count the 
numbers of characters in the string
 and store them in a dictionary data structure.'''
str=input("enter string: ")
f={}
for i in str:
    if i in f.keys():
        f[i]+=1
    else:
        f[i]=1
print(f)