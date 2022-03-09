print("**********************************************************************")
print("Este código pede 3 números, calcula o quadrado deles e soma todos eles")
print("**********************************************************************")
print()

numero_str = input("Digite o primeiro número: ")
numero_1 = float(numero_str)
quadrado_numero_1 = numero_1 * numero_1
print()
numero_str = input("Digite o segundo número: ")
numero_2 = float(numero_str)
quadrado_numero_2 = numero_2 * numero_2
print()
numero_str = input("Digite o terceiro número: ")
numero_3 = float(numero_str)
quadrado_numero_3 = numero_3 * numero_3
print()
soma_total = quadrado_numero_1 + quadrado_numero_2 + quadrado_numero_3
print("A soma dos quadrados dos três valores é: ", soma_total)