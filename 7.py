import random

a = int(input("введите длину требуемого списка "))
list = [random.randint(1, 50) for a in  range(a)]
print(list)