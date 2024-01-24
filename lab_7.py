# 7. Write a program for filter() to filter only even numbers from a given list.

def even(x):
    return x % 2==0
a=[2,5,7,8,10,13,16]

result=filter(even,a)
print("Original list: ",a)
print("Filtered list: ",list(result))