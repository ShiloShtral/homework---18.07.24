import statistics

list1 = []

while True:
    temp = float(input("Type in the temperature : "))
    if temp == -999:
        break
    if temp < -50 or temp > 50:
        break
    list1.append(temp)

additional_temp = [-20.0, 39.1, 18.5]
list1.extend(additional_temp)

print("List of temperatures:", list1)

print("The biggest temperature in the list:", max(list1))
print("The smallest temperature in the list:", min(list1))

average_temp_mean = statistics.mean(list1)
print(f"The average temperature is: {average_temp_mean:.2f}")

del list1[0]
print("The list after removing the first temperture : ", list1)

list1.remove(18.5)
print("The list after removing 18.5 from the list : " , list1)

last_temp = list1.pop()
print("the list after removing the last temperature :" , list1)

copy_list = list1.copy()

copy_list.sort()
print("The copied list after sort : " ,list1)

copy_list.sort(reverse=True)
print("The copied list after reverse sort : " , copy_list)
# ההבדל בין sort ל sorted הוא שבsort הרשימה המקורית משתנית .
# בsorted חוזרת רשימה חדשה ממויינת


reversed_copy_list = list(reversed(copy_list))
print("The reversed copied list : " , reversed_copy_list)


