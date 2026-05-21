#Error  comun de principiante
respuesta_Usuario ="False" #Esto es texto

#La función evalua si el string esta vacio
es_verdad = bool(respuesta_Usuario)

print("El valor es: ",es_verdad)

#Output: El valor es: true
# ¿Por que? Porque el string "False" tiene 5 letras. No esta vacío
#Forma Correcta de validar vació
texto_Vacio = ""
print(bool(texto_Vacio)) #False