def palindromo(palabra):
    palabra= palabra.replace(' ','')
    palabra= palabra.lower()# pone la palabra en miniscula con lower
    palabra_invertida= palabra[::-1] #esta se usa para leer el caracter desde el final hacia el inicio
    if palabra == palabra_invertida:
        return True
    else:
         return False   
    

def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print(' No es palindromo')


if __name__=='__main__': #estandar en la comunidad de lenguaje paython, se llama entriponint, es el punto de entrada de todo programa
    run()
 