# * my_mayor v1 (https://github.com/aguascesar/2024-FSP_M3d9-SentCondItera-DF-Sentencias2-byCesarAguas-v1)
# * Copyright 2024 Cesar Aguas
# * Licensed under AGPL3.0 (https://github.com/aguascesar/2024-FSP_M3d9-SentCondItera-DF-Sentencias2-byCesarAguas-v1/LICENSE)
#   
#   Filtrado compacto
#Se solicita devolver un informe resumido que exponga los meses que superan un cierto
#umbral. El programa mayor_a.py debe retornar un diccionario con el mes y el valor
#asociado siempre y cuando superen el umbral especificado.
import sys

# Diccionario local
ventas = {
 "Enero": 15000,
 "Febrero": 22000,
 "Marzo": 12000,
 "Abril": 17000,
 "Mayo": 81000,
 "Junio": 13000,
 "Julio": 21000,
 "Agosto": 41200,
 "Septiembre": 25000,
 "Octubre": 21500,
 "Noviembre": 91000,
 "Diciembre": 21000,
}

# Función para buscar los meses que superan la cantidad ingresada
def buscando(cantidad):
    # Debemos guardar la busqueda
    encontrados = {}
    # Registrando el diccionario
    for i, j in ventas.items():
        if j > cantidad:
            encontrados[i] = j
    return encontrados

# Función principal
def main():
    if len(sys.argv) != 2:
        print("Por favor escriba: python mayor_a.py [Cantidad]")
        return

    cantidad = int(sys.argv[1])

    # Buscar coincidencias
    encontrados = buscando(cantidad)

    # Imprimir el resultado
    print(encontrados)


# Ejecutando
main()
