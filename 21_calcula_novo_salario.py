print("*************************************************")
print("Este código devolve o novo salário d@ funcionári@")
print("*************************************************")

print("\nEstes são nossos planos disponíveis: \n")
print("| Plano |Aumento|")
print("|   A   |   10% |")
print("|   B   |   15% |")
print("|   C   |   20% |")

plano = input('\nInforme o plano atual d@ funcionári@: \n')

salarioinicial = float(input('\nInforme o salário atual d@ funcionári@: \nR$'))

if plano == 'A':
  salariofinal = salarioinicial * 1.1
  print('\nO salário atualizado será de: R${:.2f}'.format(salariofinal))
  pass
  
elif plano == 'B':
  salariofinal = salarioinicial * 1.15
  print('\nO salário atualizado será de: R${:.2f}'.format(salariofinal))
  pass
  
elif plano == 'C':
  salariofinal = salarioinicial * 1.2
  print('\nO salário atualizado será de: R${:.2f}'.format(salariofinal))
  pass
  
else:
  print('\nPlano não identificado, tente novamente.')
  pass

print('\n\nFim do código.')
