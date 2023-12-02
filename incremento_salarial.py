#KPC
#El objetivo de este codigo es calcular el incremento salarial de una persona, bajo la condición 
#que si su salario es menor a 15 mil el incremento será del 20% y si es mayor a 15 mil el incremento será de 10%

def calcular_incremento_salarial(salario_actual):
    umbral_superior = 15000
    tasa_incremento_mayor = 0.20
    tasa_incremento_menor = 0.10
    
    if salario_actual <= umbral_superior: 
        incremento = salario_actual*tasa_incremento_mayor
    else: 
        incremento = salario_actual*tasa_incremento_menor
    nuevo_salario = incremento + salario_actual 
    return incremento, nuevo_salario 

salario_actual= float(input("Ingresa tu salario actual "))

incremento, nuevo_salario = calcular_incremento_salarial(salario_actual)
print(f"Tu incremento salarial es de: {incremento}")
print(f"Tu nuevo salario es: {nuevo_salario}")





