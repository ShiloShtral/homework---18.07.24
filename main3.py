import random

boolist = [random.choice([True,False]) for _ in range(3)]
print("Bolean list : ", boolist)

print("Does the list contain only True?", all(boolist))

print("Does the list contain at least one True?" , any(boolist))

print("Does the list contain only False?" , not any(boolist))

print("Does the list contain at least one false?" ,not all(boolist))


newlist = [random.randint(-2, 2) for _ in range(5)]
print("Number list:", newlist)

print("Does the list contain different numbers then 0 ? :" , all(x != 0 for x in newlist))

print("Does the list contain only non-zero numbers?", all(x != 0 for x in newlist))

print("Does the list contain only zero? : ", all(x == 0 for x in newlist))

print("Does the list contain at least one zero? :" , any(x == 0 for x in newlist))

