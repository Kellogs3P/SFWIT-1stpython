#KPC
#El objetivo de este codigo es recibir la velocidad 
#y la distancia que tiene que recorrer un carro y entregar cuanto tiempo le tomaria recorrer esa distancia 

def calcular_tiempo(velocidad,distancia):
    tiempo=distancia/velocidad
    return tiempo 

cuanta_velocidad = float(input("Hola, introduce la velocidad, por favor "))
cuanta_distancia= float(input("introduce la distancia "))

print(f"El tiempo que se tomó el coche en recorrer {cuanta_distancia} km con una velocidad de {cuanta_velocidad} km/h es {calcular_tiempo}")