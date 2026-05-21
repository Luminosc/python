#Sistema Generador ID Unico
#Con los datos recibidos el sistema deberá realizar los siguientes:
#1. Del valor recibido de nombre, usar solo las 2 primeras letras y convertirlas a mayúsculas
#2. Del valor de Apellido, Usar las 2 primeras letras y convertirlas a mayúsculas
#3. Del valor de año tomar los últimos dos dígitos
#Además el sistema deberá generar un valor aleatorio de 4 dígitos con ayuda de la función randint
#Finalmente con los datos obtenidos generar un ID único uniendo los valores como Sigue:
#Ejemplo    Nombre: Juan >              JU
#           Apellido: Perez >           PE
#           Nacimiento: 1995 >          95
#           Valor aleatorio: randint >  1548
#     Resultado ID Unico JUPE951548

from random import randint

print("**********************Generador de ID Único**********************")
Nombre = input("Ingrese su primer nombre: ")
Apellido = input("Ingrese su primer apellido: ")
Anio = input("Ingrese su año de nacimiento: ")
rando = str(randint(1,9999)).zfill(4)

ID = Nombre.upper()[:2] + Apellido.upper()[:2] + str(Anio).upper()[-2:] + rando
print("ID: ", ID)