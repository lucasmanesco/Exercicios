n1, n2, n3, n4 = input().split()

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = ((2 * n1) + (3 * n2) + (4 * n3) + (1 * n4)) / (2 + 3 + 4 + 1)

print('Media: %.1f' % media)

if media >= 7:
    print('Aluno aprovado.')
else:
    if media < 5:
        print('Aluno reprovado.')
    else:
        print('Aluno em exame.')
        ne = float(input())
        print('Nota do exame: %.1f' % ne)
        media_final = (media + ne) / 2
        if media_final >= 5:
            print('Aluno aprovado.')
            print('Media final: %.1f' % media_final)
        else:
            print('Aluno reprovado.')
            print('Media final: %.1f' % media_final)