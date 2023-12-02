#KPC
#La finalidad de este codigo es definir si un numero es par o impar

def identificar_parimpar (numero):
    if numero % 2 == 0: 
        return par
    else: 
        return impar 

numero_ingresado=int(input"Hola, ingresa un numero entero por favor")

resultado=identificar_parimpar(numero_ingresado)

print(f"El numero que ingresaste se identifica como {resultado}")