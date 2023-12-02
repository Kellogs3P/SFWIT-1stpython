#KPC
#La finalidad del sig. codigo es calcular el número de días que alguien ha vivido tomando en cuenta su fecha de nacimiento

from datetime import datetime

def calcular_días_vividos (fecha_nacimiento):
    fecha_nacimiento =datetime.strptime(fecha_nacimiento,"%Y-%m-%d")

    fecha_actual= datetime.now()

    diferencia= fecha_actual - fecha_nacimiento

    dias_totales= diferencia.days 

    return dias_totales 

fecha_nacimiento_usuario = input("Hola, ingresa tu fecha de nacimiento bajo el siguiente formato yyyy-mm-aa por favor")

dias_totales = calcular_días_vividos(fecha_nacimiento_usuario)
print (f"Los días totales que has vividos hasta hoy, son {dias_totales} dias") 