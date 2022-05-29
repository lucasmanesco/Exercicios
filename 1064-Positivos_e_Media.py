i = 0
positivos = 0
soma = 0

while i < 6:
    n = float(input())
    if n > 0:
        positivos += 1
        i += 1
        soma = soma + n
    else:
        i += 1

media = soma / positivos

print(positivos, 'valores positivos')
print(media)