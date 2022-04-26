cod1, qtd1, val1 = input().split()
cod2, qtd2, val2 = input().split()

cod1 = int(cod1)
cod2 = int(cod2)
qtd1 = float(qtd1)
qtd2 = float(qtd2)
val1 = float(val1)
val2 = float(val2)

total = (val1 * qtd1) + (val2 * qtd2)

print('VALOR A PAGAR: R$ %.2f' % total)