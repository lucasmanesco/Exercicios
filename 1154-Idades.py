soma = 0
qtd = 0

n = int(input())

while n >= 0:
    soma = soma + n
    qtd = qtd + 1
    n = int(input())

media = soma / qtd

print('%.2f' % media)