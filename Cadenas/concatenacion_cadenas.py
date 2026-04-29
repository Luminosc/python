#Programa: Ejemplo de concatenación de cadenas.

#1.- Usando el operador +

nombre ="Lucia"
apellido ="Garcia"
nombre_completo = nombre + " "+ apellido
print(nombre + " " + apellido + " " + nombre_completo)

#2.- Usando el metodo print

edad = 28

print("Usando Comas, Nombre: ",nombre," " , apellido , " Edad"," ", edad)

#3.- Usando f-Strings
ciudad = "CDMX"
pais = "México"
profesion = "Ingenieria"

presentacion = f"Hola, soy {nombre_completo}, tengo {edad} años, soy de {ciudad}, {pais} y tengo la profesion de {profesion}"
print(presentacion)