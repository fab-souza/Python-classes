print("************************************************************************")
print("Este código pede 2 valores e imprime se a soma deles for maior do que 10")
print("************************************************************************")
print()

A_str = input("Digite o 1º número inteiro: ")
A = int(A_str)

B_str = input("Digite o 2º número inteiro: ")
B = int(B_str)

soma = A + B

if(soma > 10):
  print("O valor da soma é maior do que 10.")
