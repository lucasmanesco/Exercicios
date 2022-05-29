n = int(input())

ano = n // 365
n = n - (ano * 365)
print(ano, 'ano(s)')

mes = n // 30
n = n - (mes * 30)
print(mes,'mes(es)')

dia = n // 1
n = n - (dia * 1)
print(dia, 'dia(s)')