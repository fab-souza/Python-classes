print("**************************************************")
print("Este código pede 10 números e imprime a soma deles")
print("**************************************************\n")

contador = 10
numeros = []

for i in range (contador):
  numeros.append(int(input('Digite o número: ')))

listSum = 0

listSum = sum(numeros)
print("\nA soma da lista é {}".format(listSum))


print('\n\nFim do código.')
