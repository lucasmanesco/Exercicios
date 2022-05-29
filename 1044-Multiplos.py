a, b = input().split()

a = int(a)
b = int(b)

if a > b:  
    if a % b == 0:
        print('São Múltiplos')
    else:
        print('Não são Múltiplos')
else:
    if b % a == 0:
        print('São Múltiplos')
    else:
        print('Não são Múltiplos')