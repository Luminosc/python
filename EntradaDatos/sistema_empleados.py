#Crea un programa para solicitar la información de un empleado, introducción de un empleado, instroduciendo los datos por consola
#Nombre Empleado
#Edad del empleado (convertir a entrero)
#Salario del empleado (convertir a flotante)
#Es jefe de departamento

print("Sistema de registro de empleados \n\n\n")

#Para Nombre de empleado
Nombre = str(input("Nombre Completo: "))
#Para Edad de empleado
Edad = int(input("Edad: "))
#Para Salario de empleado
salario = float(input("Salario: "))
#Para saber si es jefe de departamento o no
jefet = str(input("Jefe (Y/N): "))
jefe = False
if jefet == "Y":
    jefe = True
elif jefe == "N":
    jefe = False

print("\nDatos del empleado")
print (f"Nombre: {Nombre}")
print (f"Edad: {Edad}")
print (f"Salario: ${salario:.2f}")
print (f"¿Es jefe de dapartamento?: {jefe}")