
list1 = []

for i in range(80,100):
    list1.append(i)

print("The first element in the list : ",list1[0])

print("The last element in the list :",list1[-10])

print("Number of elements in the list : ",len((list1)))

print("The elements fron index 3 to 12 : " ,list1[3:13])

print("The elements fron index 3 to the end : " ,list1[3:])

print("The element fron the beginning to index 9 : ",list1[:9])

middle_list = len(list1) // 2
list1.insert(middle_list, 999)
print("The list after inserting 999 in the middle : " , list1)

print("The list from end to start : " ,list1[::-1])

print("The odds elements : " ,list1[1::2])

