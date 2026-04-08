#Programa: Reghiistro de exploración espacial
from tipo_datos import misiones_completadas, nivel_energia

#Asignar valores a las variables

nombre_explorador ="Luna Vega"
planeta_origen = "Marte"
edad_explorador = 29
misiones_completadas = 4
nivel_explorador = 87.5

#for = 15 esto arroja error

Nivel_Energia = 90.5 #No es una buena practiva
NIVEL_ENERGIA = 100 #Se considera una constante.
nivel_energía = 80.0 #No se deben usar caracteres especiales

print("=== Registro Espacial ===")
print("Eombre: ", nombre_explorador)
print("Edad: ", edad_explorador)
print("Misiones: ", misiones_completadas)
print("Nivel: ", nivel_explorador)

print("Nivel de Enería: ", Nivel_Energia)
print("NIVEL_ENERGIA: ", NIVEL_ENERGIA)
print("nivel_energia: ", nivel_energía)
