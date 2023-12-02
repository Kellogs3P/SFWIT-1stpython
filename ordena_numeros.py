#KPC
#La finalidad de este codigo es ordenar 5 numeros del mayor al menor 

numeros = []

for i in range(5):
    numero = float(input("Ingrese un número: "))
    numeros.append(numero)

# Ordena los números de manera ascendente
numeros_ordenados = sorted(numeros)

# Imprime los números ordenados
print("Números ordenados:", numeros_ordenados)
