#KPC
#El objetivo del sig. codigo es que calcule el volumen de una esfera

import math
#de aqui se va a tomar pi para la formula 
#formula del volumen de la esfera V=4/3piR^3

def calcular_volumen_esfera(radio):
    volumen = 4/3*math.pi*radio**3
    return volumen

radio_esfera = float(input("Hola, ingresa el radio de la esfera por favor "))

volumen_esfera = calcular_volumen_esfera(radio_esfera)
print(f"El volumen de la esfera con radio {radio_esfera} es: {volumen_esfera}")

