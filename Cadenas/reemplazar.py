#Programa: Reemplazr texto en python

mensaje = "Hola Mundo, Mundo"

#Reemplaza todas las apariciones

nuevo = mensaje.replace("Mundo", "Pyhton")
print(mensaje)
print(nuevo)

#Reemplaza solo una vez

uno_solo = mensaje.replace("Mundo", "Dev",1)
print(uno_solo) #Hola Dev, Mundo