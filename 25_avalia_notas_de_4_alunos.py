print("******************************************************")
print("Este código devolve se 4 alun@s passaram de ano ou não")
print("******************************************************\n")

contador = 1

while (contador < 5):
  nome = input('\n\nDigite o nome d@ alun@: \n')
  nota1 = float(input('\nDigite a nota 1 (de 0 à 10): \n'))
  nota2 = float(input('\nDigite a nota 2 (de 0 à 10): \n'))
  nota3 = float(input('\nDigite a nota 3 (de 0 à 10): \n'))
  media = (nota1 + nota2 + nota3) / 3
  print("\nCom a média de {:.2f}".format(media))
  
  if(media >= 7.0):    
    print("\nAlun@ {}, passou de ano.\n".format(nome))
    pass
    
  elif(media >= 5.0 and media < 7.0):
    print("\nAlun@ {}, está de recuperação.\n".format(nome))
    pass

  else:
    print("\nAlun@ {}, reprovou.\n".format(nome))
    pass
  
  contador = contador + 1

print('\n\nFim do código.')
