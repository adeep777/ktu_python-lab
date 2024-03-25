#def insert_at_end(array, element):
#array.append(element)


array = [1, 2, 3, 4, 5]
element = 6
print(array)
element=int(input("enter the element to be inserted at the end"))
array.append(element)
index=int(input("enter the index to be inserted"))
element=int(input("enter the element to be inserted at the index"))
array.insert(index,element)
#insert_at_end(my_array, new_element)
print("array after inserting:",array)
array.pop()
print("array after deleting at the end",array)
index=int(input("enter the index to be deleted"))
array.pop(index)
print("array after deleting from the index",array)
