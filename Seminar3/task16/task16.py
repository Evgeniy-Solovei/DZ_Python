# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 12345
# 3 -> 1

from random import randint
n = int(input())
number = []
for i in range(n):
    number.append(randint(0, 10))
print(number, '\n')
x = int(input())
print()
print(number.count(x))


# sequence = list(map(int, input().split()))     --------- заполнение списка
# sequence = input().split()
# sequence = map(int, sequence)
# sequence = list(sequence)
# print(sequence)
