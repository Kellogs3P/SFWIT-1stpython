#KPC
#El objetivo de este codigo es calcular el área de un triangulo 

def calcular_area_triangulo(base,altura): 
    area = base* altura* 0.5
    return area

base_triangulo=float(input("Hola, ingresa la base del triangulo "))
altura_triangulo=float(input("ahora ingresa la altura del triangulo"))

area_triangulo= calcular_area_triangulo(base_triangulo,altura_triangulo)

print(f"El área del triangulo es {area_triangulo}")