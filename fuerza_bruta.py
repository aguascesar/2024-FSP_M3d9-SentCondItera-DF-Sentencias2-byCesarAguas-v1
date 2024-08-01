# * my_encontrador v1 (https://github.com/aguascesar/2024-FSP_M3d9-SentCondItera-DF-Sentencias2-byCesarAguas-v1)
# * Copyright 2024 Cesar Aguas
# * Licensed under AGPL3.0 (https://github.com/aguascesar/2024-FSP_M3d9-SentCondItera-DF-Sentencias2-byCesarAguas-v1/LICENSE)
#   
#   Fuerza bruta
#Determinar cuántos intentos son necesarios para encontrar combinaciones numéricas en
#minúscula. El programa fuerza_bruta.py debe intentar todas las combinaciones de letras
#posibles, en orden alfabético, hasta que la combinación de letras sea igual a la de la
#contraseña indicada. Deberá hacer este proceso letra por letra, de izquierda a derecha.


from string import ascii_lowercase          #Necesitamos un diccionario con el abecedario, en este caso minusculas
import getpass                              #Se necesita para ingresar la clave sin que sea vista
import sys                                  #Se necesita para ingresar argumentos


#   Funcion para buscar las coincidencias
def buscando(clave):
    veces = 0
    for i in clave:
        print(f"{veces} veces, Letra: {i}")
        for letra in ascii_lowercase:      #Llega el momento de comparar
            veces += 1
            if i == letra:
                break
    return veces

#   Se necesita una funcion principal
def main():
    clave = getpass.getpass("Ingrese una clave: ").lower()
    if len(sys.argv) == 2:
        clave = sys.argv[1].lower()
    else:
        print("Ingrese una clave valida: ")
    
    #Ejecutando la busqueda de coincidencias (funcion)
    veces = buscando(clave)
    print(f"La contraseña fue encontrada en {veces} iteraciones.")

#   Ejecutando funcion principal
main()