#Receta de Cocina
#Crear un programa para colicitar algunos valores importantes para una recesta de cocina
#Los valores que debe introducir el usuario son:
#-Nombre de la receta
#-Ingredientes
#Tiempo de Preparación (En minutos)
#Dificultad (Facil, Mediana, Alta)
#Mandar a imprimir la receta.

print("***Receta de Cocina***")
nombre_receta = input("¿Cual es el nombre de la receta?: ")
Ingredientes = input("Ingredientes: ")
Tiempo_preparacion = int(input("Tiempo de preparación en minutos: "))
Dificultad = int(input("""Dificultad:
1.Facil
2.Meio
3.Dificil
Escoge dificultad por numero: """))

print(f"""\n\n\n///Datos de la receta///
Receta: {nombre_receta}
Ingredientes: {Ingredientes}
Tiempo de preparación en minutos: {Tiempo_preparacion}""")
if Dificultad==1:
    print("Dificultad: Facil")
elif Dificultad==2:
    print("Dificultad: Meio")
elif Dificultad==3:
    print("Dificultad: Dificil")