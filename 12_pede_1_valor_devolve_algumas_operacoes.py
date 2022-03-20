print("***********************************************************")
print("Este código pede 1 valor e efetua algumas operações com ele")
print("***********************************************************")
print()

A_str = input("Digite 1 número inteiro: ")
A = int(A_str)

B = 3*A + 1
C = 2*A - 1
final = B + C

print()
print("O triplo do valor mais 1 é de {}.".format(B))
print()
print("O dobro do valor menos 1 é de {}.".format(C))
print()
print("A soma dos 2 últimos valores é de {}.".format(final))
