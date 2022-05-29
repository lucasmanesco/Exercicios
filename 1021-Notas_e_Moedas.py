n = float(input())

print('NOTAS:')

c100 = int(n // 100)
n = n - (c100 * 100)
print(c100, 'nota(s) de R$ 100.00')

c50 = int(n // 50)
n = n - (c50 * 50)
print(c50, 'nota(s) de R$ 50.00')

c20 = int(n // 20)
n = n - (c20 * 20)
print(c20, 'nota(s) de R$ 20.00')

c10 = int(n // 10)
n = n - (c10 * 10)
print(c10, 'nota(s) de R$ 10.00')

c5 = int(n // 5)
n = n - (c5 * 5)
print(c5, 'nota(s) de R$ 5.00')

c2 = int(n // 2)
n = n - (c2 * 2)
print(c2, 'nota(s) de R$ 2.00')

print('MOEDAS:')

c1 = int(n // 1)
n = n - (c1 * 1)
print(c1, 'moeda(s) de R$ 1.00')

c05 = int(n // 0.5)
n = n - (c05 * 0.5)
print(c05, 'moeda(s) de R$ 0.50')

c025 = int(n // 0.25)
n = n - (c025 * 0.25)
print(c025, 'moeda(s) de R$ 0.25')

c01 = int(n // 0.10)
n = n - (c01 * 0.10)
print(c01, 'moeda(s) de R$ 0.10')

c005 = int(n // 0.05)
n = n - (c005 * 0.05)
print(c005, 'moeda(s) de R$ 0.05')

c001 = int(n // 0.01)
n = n - (c001 * 0.01)
print(c001, 'moeda(s) de R$ 0.01')