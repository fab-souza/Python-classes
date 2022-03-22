print("*************************************************")
print("Este código devolve o maior valor entre 3 números")
print("*************************************************")

numero1 = int(input('\nDigite 1 número inteiro: '))
numero2 = int(input('\nDigite o 2º número inteiro: '))
numero3 = int(input('\nDigite o último número: '))

if numero1>numero2 and numero1>numero3:
  print('\nO 1º número é o maior entre os 3 digitados: {}'.format(numero1))

elif numero2>numero1 and numero2>numero3:
  print('\nO 2º número é o maior entre os 3 digitados: {}'.format(numero2))
  
else:
  print('\nO 3º número é o maior entre os 3 digitados: {}'.format(numero3))
