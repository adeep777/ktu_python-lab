string = "HappyNewYear"
p = ""
for char in string:
    if char not in p:
        p = p+char
print(p)
