print("**************************************")
print("Este código verifica a idade da pessoa")
print("**************************************")

idade = int(input('\nDigite a idade da pessoa: '))

if(idade>=18):
  restante = idade - 18
  print('A pessoa tem direito a habilitação à {} anos.'.format(restante))

else:
  restante = 18 - idade;
  print('Faltam {} anos para a pessoa poder tirar a habilitação.'.format(restante))
