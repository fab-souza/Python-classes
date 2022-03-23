import math

print("**************************************************************")
print("Este código devolve diâmetro, circunferência e área do círculo")
print("**************************************************************")

raio = float(input('\nDigite o valor do raio (cm): \n'))

diametro = raio * 2
circunferencia = diametro * math.pi
area = (math.pi) * (raio*raio)

print('\nCom um raio de {:.3f}, tem-se: \n'.format(raio))
print('\nO diâmetro é de {:.3f}cm.'.format(diametro))
print('\nA circunferência é de {:.3f}cm.'.format(circunferencia))
print('\nA área é de {:.3f}cm².'.format(area))

print('\n\nFim do código.')
