print("***************************************************")
print("Este código verifica as notas e frequência d@ alun@")
print("***************************************************")

nota1 = float(input('\nDigite a 1ª nota (de 0.0 a 10.0): '))
nota2 = float(input('\nDigite a 2ª nota (de 0.0 a 10.0): '))

frequencia = float(input('\nDigite o valor equivalente a porcentagem de frequência registrada pel@ alun@: \n'))

media = (nota1 + nota2) / 2

if media>=7.0 and frequencia>=75:
  print('\nMedia suficiente e frequência OK. \nPassou de ano.')
  
elif media<=7.0 or frequencia<75:
  print("\nMedia insuficiente ou frequência baixa. \nReprovou...")
