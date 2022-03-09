print("*****************************************************************************")
print("Este código pede uma temperatura em Celsius e devolve seu valor em Fahrenheit")
print("*****************************************************************************")
print()
celsius_str = input("Digite a temperatura em Celsius: ")
celsius = float(celsius_str)
fahrenheit = (celsius * 9/5) + 32
print("A temperatura em Fahrenheit é de: ", fahrenheit)
