
list1 = [10,20,30,40]


while True:
    try:
        index = int(input("type in an index (Type -999 to exit) : "))

        if index == -999:
            break

         print(f"The element at index {index} is : {list1[index]} ")

    except ValueError:
    print("Error - Enter a valid number")

