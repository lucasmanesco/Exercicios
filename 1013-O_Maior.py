import math

a, b, c = input().split()

a, b, c = int(a), int(b), int(c)

maior_ab = (a + b + abs(a - b))  / 2
maior = (maior_ab + c + abs(maior_ab - c)) / 2

maior = int(maior)

print(maior, 'eh o maior')