import random

num_list = [num for num in range(95, 106)]
print("The list from 95 to 105  is :" , num_list)

listnum = [ num for num in range(10, 21) if num % 2 == 0]
print("The even numbers from 10 to 20 is : " , num_list)

boolist = [random.choice([True, False]) for _ in range(5)]
print("Random boolean list : " , boolist)

# משתמשים ב_ כי הוא עוזר להבין את הקוד ומונע בלבול

random_list = [random.randint(1, 100) for _ in range(10)]
print(random_list)
