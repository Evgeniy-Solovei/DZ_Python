# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes 3 2 1 -> no

m, n, k = int(input('Введите размер шоколадки m: ')), int(input('Введите размер шоколадки n: ')), int(input('Введите количество долек k: '))
if (k == m or k == n) or (k % m == 0 or k % n == 0) and k < m*n:
    print('yes')
else:
    print("no")

# Задача с уловием Да-К может быть либо = m или n или должно быть больше n и m, но должно быть кратно m и n.
