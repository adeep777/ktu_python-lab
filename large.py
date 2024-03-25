

name= ['a',' d','e', 'e', 'p']


print ("String is : ",name)


max = 0
res = name[0]
for i in name:
    freq = name.count(i)
    if freq > max:
        max = freq
        hfreq = i


print ("highest frequent element is : ",hfreq)
