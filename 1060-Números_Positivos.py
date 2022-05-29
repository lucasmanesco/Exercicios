i = 0
positivos = 0

while i < 6:
    n = float(input())
    if n > 0:
        positivos += 1
        i += 1
    else:
        i += 1

print(positivos, 'valores positivos')