tempo = int(input())
vel_media = int(input())

consumo = 12.0

distancia = vel_media * tempo

litros = distancia / consumo

print('%.3f' % litros)