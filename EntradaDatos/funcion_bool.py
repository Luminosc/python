#Programa: Función bool

#1. Numero (Int y Folat)

print (bool(0)) #False (El vacio numerico)

print (bool(0.0)) #False

print(bool(404)) #True (Existe Valor)

#2. Texto (String)

#Cadena vacía = Nada = False

print(bool("")) #False

#Cadena con espacio o Texto = Algo = True

print(bool(" "))
print(bool("Hola mundo"))

#3 None (Ausencia total)

vacio = None

print(bool(vacio)) #False


print(bool(False))