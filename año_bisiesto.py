#KPC
#El objetivo de este codigo es determinar si un año es bisiesto o no bisiesto 

def verificar_año(año):
    if año % 4 == 0 and año % 100 != 0:
        print(f"Este {año} año es bisiesto")
    else: 
        print(f"Este {año} año es no bisiesto")

año_ingresado=int(input("Ingresa un año "))

verificar_año(año_ingresado)