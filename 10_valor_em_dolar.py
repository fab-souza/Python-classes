print("********************************************************")
print("Este código pede um valor em reais e converte para dólar")
print("********************************************************")
print()

real_str = input("Digite o valor em reais: ")
real = float(real_str)
print()
cotacao_str = input("Digite o valor da cotação do dólar: ")
cotacao = float(cotacao_str)
print()
dolar = real / cotacao
print("O valor correspondente em dólar é de US${:.4}".format(dolar))