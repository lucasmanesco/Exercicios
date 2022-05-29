n = int(input())

hora = n // 3600
n = n - (hora * 3600)

minuto = n // 60
n = n - (minuto * 60)


segundo = n // 1
n = n - (segundo * 1)

print(repr(hora)+":"+repr(minuto)+":"+repr(segundo))


# print(hora,':',minuto,':',segundo)