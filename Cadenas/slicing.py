#Programa: Aplicar el concepto de slicing

texto = "PROGRAMACIÓN"

#1. Basico [Inicio:Fin]

print(texto[0:4]) #PROG

#2. Atajo desde el Inicio [:Fin]

print(texto[:4])

#3. Atajo hasta el final [Inicio]

print(texto[8:])

#4. Indice Negativo
print(texto[-4:])


#5. pASOS [::paso] (Invertir cadena)

print(texto[::-1]) #NÓICAMARGORP

print(texto[::2]) #PORMCÓ