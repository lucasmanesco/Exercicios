i = 0
pares = 0

while i < 5:
    n = float(input())
    if n % 2 == 0:
        pares += 1
        i += 1
    else:
        i += 1

print(pares, 'valores pares')