
# Metodos de cadena de tetxo
# variable.upper() = 'todos los caracteres en MAYÚSCULAS'
# variable.capitalize() = 'solo la primera en MAYÚSCULA'
# variable.lower() = 'todos los caracteres en minúscula'
# variable.strip() = 'eliminar espacios basura del string'
# variable.replace('caractera a cambiar', 'caracter por poner') = remplazar caracter

nombre1= "david  urrego:"
nombre1= nombre1.upper()

nombre2= "david  urrego:"
nombre2= nombre2.capitalize()

nombre3= "DAVID  URREGO:"
nombre3= nombre3.lower()

nombre4= " DAVID  urrego: "
nombre4= nombre4.strip()

nombre5= " DAVID  urrego: "
nombre5= nombre5.replace("A","E")
nombre6= "David"
nombre6= nombre6[0]
nombre7= "David"

print (nombre1+ " todos los caracteres en MAYÚSCULAS")
print (nombre2+ " muestra solo la primera en MAYÚSCULA")
print (nombre3+ " muestra todos los caracteres en minúscula")
print (nombre4+ " eliminar espacios basura del string")
print (nombre5+ " remplaza caracter a por caracter b ")
print (nombre6+ " Devuelve la letra con el indice ")
print (len(nombre7)) #" retorna  la cantidad de caracteres "

#Trabajando con texto: slices

# apellido="Montoya"

# apellido[1]
# apellido[1:3]
# apellido[1:3:2] # del carecter inciio al final, de dos en dos



