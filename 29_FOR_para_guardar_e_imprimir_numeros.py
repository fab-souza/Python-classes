print("***********************************************")
print("Este código pede 10 números e depois os imprime")
print("***********************************************\n")

contador = 10
numeros = []

for i in range (contador):
  numeros.append(input('Digite o número: '))

print('\nOs números são:')
for indice, numero in enumerate(numeros):
  print(indice, '->', numero)

print('\n\nFim do código.')
