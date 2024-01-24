'''4. Create a dictionary and apply the following methods
1) Print the dictionary items
2) access items
3) use get()
4)change values
5) use len()'''

print("performing with dictionary")

dict1={"name":"suma","regno":"023","course":"BCA","age":19}

print(dict1)

print('accessing the items:')
print(dict1["age"])
print('using get():')
x=dict1.get("regno")
print(x)
print('changing the values in the dictionary:')
dict2={"regno":286}
dict1.update(dict2)
print(dict1)
print('length of dictionary is:',len(dict1))