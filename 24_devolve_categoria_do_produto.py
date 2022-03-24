print("******************************************")
print("Este código devolve categoria dos produtos")
print("******************************************\n")

print("============================================")
print("|         Tabela       de      produtos    |")
print("============================================")
print("| Código |                   Classificação |")
print("|   01   |          Alimento não perecível |")
print("|   02   |              Alimento perecível |")
print("|   03   |              Alimento perecível |")
print("|   04   |              Alimento perecível |")
print("|   05   |                       Vestuário |")
print("|   06   |                       Vestuário |")
print("|   07   |                 Higiene pessoal |")
print("|   08   | Limpeza e utensílios domésticos |")
print("|   09   | Limpeza e utensílios domésticos |")
print("|   10   | Limpeza e utensílios domésticos |")
print("|   11   | Limpeza e utensílios domésticos |")
print("|   12   | Limpeza e utensílios domésticos |")
print("|   13   | Limpeza e utensílios domésticos |")
print("|   14   | Limpeza e utensílios domésticos |")
print("|   15   | Limpeza e utensílios domésticos |")
print("| Outros |                 Código inválido |")
print("============================================\n\n")

codigo = input('Digite o código do produto: ')

if codigo == '1':
  print("\nA classificação do produto é: \nAlimento não perecível.")
  pass

elif codigo == '2' or codigo == '3' or codigo == '4':
  print("\nA classificação do produto é: \nAlimento perecível.")
  pass

elif codigo == '5' or codigo == '6':
  print("\nA classificação do produto é: \nVestuário.")
  pass

elif codigo == '7':
  print("\nA classificação do produto é: \nHigiene pessoal.")
  pass

elif codigo == '8' or codigo == '9' or codigo == '10' or codigo =='11' or codigo == '12' or codigo == '13' or codigo == '14' or codigo == '15':
  print("\nA classificação é de: \nLimpeza e utensílios domésticos.")
  pass

else:
  print('\nCategoria inválida!\n')
  pass

print('\n\nFim do código.')
