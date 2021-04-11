def conversor (valor_dolar, tipo_pais):
    pesos = int(input("¿Cuántos pesos "+tipo_pais+" tienes?"))
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)  
    dolares = str(dolares)
    print("Tienes $" + dolares + "dorales")

menu =""" 
Bienvenmido al conversor de moneda.

1-Pesos colombianos
2-Pesos argentinos
3-Pesos mexicanos

Eleige una opción: """ #Se puede utilizar 6 comillas para hacer una cadena en serie o varias lineas.

opcion = int(input(menu))

if opcion == 1:
    conversor(3850,"Colombianos")
elif opcion == 2: #elif: se utiliza cuando utilizamos múltiples condiciones.
    conversor(91,"Argentinos")
elif opcion == 3:
     conversor(20,"Mexicanos")
else:
    print("¡Ingresa un opción correcta!")    


