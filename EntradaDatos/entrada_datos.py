#Programa: ENtrada Datos Python

nombre = input("Ingrese su nombre: ")
print("Tu nombre es " + nombre)

#Cuidado con las conversiónes de tipo al trabajar con valores numéricos
#Forma Correcta: Envolver con Int() o float()

#Para entenderlo (edad, cantidad)

edad = int(input("Ingrese su edad: "))
print(f"Tu edad es {edad}")

print(edad + 5)

#Si no pusieramos int() marcaría error por considerarlo string

#Para decimales (precio, altura)

altura = float(input("Tu altura: "))
print(f"Tu altura es {altura}m")