name=['a','d','e','e','p']
print("Name is: ",name)
newname=[]
revname=[]
for i in name:
    if i not in newname:
        newname.append(i)
print("name after duplication is",newname)
print("Array in reverse order: ");
print(newname[::-1])
