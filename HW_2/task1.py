# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию).
# Последняя строка содержит число X.
# *Пример:*
# 5
# 7 -2 3 5 1
# 3
# -> 1

import random
N = int(input('Введите кол-во элементов в массиве: '))
lst = [random.randint(0, 10) for i in range(N)]
print(lst)
X = int(input('Введите число которое нужно найти: '))
print(lst.count(X))
