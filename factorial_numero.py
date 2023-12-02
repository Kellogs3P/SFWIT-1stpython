#KPC
#La finalidad de este codigo es encontrar el factorial de cualquier número dado en python
def calcular_factorial(numero):
    if numero < 0:
        return "No se puede calcular el factorial de un número negativo"
    elif numero == 0 or numero == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, numero + 1):
            factorial *= i
        return factorial

numero_ingresado = int(input("Ingresa un número POSITIVO ENTERO para calcular su factorial: "))
resultado_factorial = calcular_factorial(numero_ingresado)

print(f"El factorial de {numero_ingresado} es: {resultado_factorial}")
