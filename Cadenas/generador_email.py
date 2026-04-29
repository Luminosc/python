#Crea un programa para generar un email a partir de los siguientes datos
#Nombr: Ubaldo Acosta Soto
#Empresa: Golbal Mentoring
#Dominio: com.mx
#Resultado Final:
#email: ubaldo.acosta.soto@globalmentorig.com.mx


#datos
nombre = "Ubaldo Acosta Soto"
Empresa = "Golbal Mentoring"
dominio = ".com.mx"
#Concatenación
email = nombre.replace(" ",".") + "@" + Empresa.replace(" ",".") + dominio

#Texto General
General = f"""
${"*"*3}Generador de Email${"*"*3}
Nombre Usuario: {nombre}
Nombre Usuario Normalizado: {nombre.lower().replace(" ",".")}

Nombre Empresa: {Empresa}
Nombre Empresa Normalizado: {Empresa.lower().replace(" ",".")}

Extensión del dominio {dominio}
Extensión de dominio Normalizado: {Empresa.lower().replace(" ",".")+dominio.lower().replace(" ",".")}


Email Final Generado ${email.lower()}
"""

print(General)