import math

a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

delta = math.sqrt((b * b) - (4 * a * c))

if delta < 0 or 2 * a == 0:
    print('Impossivel calcular')
else:
    r1 = (- b + delta) / (2 * a)
    r2 = (- b - delta) / (2 * a)
    print('R1 = %.5f' % r1)
    print('R2 = %.5f' % r2)