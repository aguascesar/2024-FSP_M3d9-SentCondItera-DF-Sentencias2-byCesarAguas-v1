# * my_primeros_auxilios v1 (https://github.com/aguascesar/2024-FSP_M3d9-SentCondItera-DF-Sentencias2-byCesarAguas-v1)
# * Copyright 2024 Cesar Aguas
# * Licensed under AGPL3.0 (https://github.com/aguascesar/2024-FSP_M3d9-SentCondItera-DF-Sentencias2-byCesarAguas-v1/LICENSE)
#   
#   Primeros auxilios
#   Se requiere la construcción de una aplicación interactiva primeros_auxilios.py que
#entregue los distintos pasos a seguir dependiendo de las respuestas que el usuario entrega
#en tiempo real.
#
#   Se necesita una funcion principal
def main():
    print("Comienzo:")
    estimulos = input("¿Responde a estimulos? [si/no]: ")

    if estimulos.lower() == "si":
        print("Valore la necesidad de llevarlo al hospital mas cercano")
        print("Fin.")
        return


    elif estimulos.lower() == "no":
        print("Encontrar la forma de abrir la vía aérea:")
        respira = input("- ¿Respira? (si/no): ")

        if respira.lower() == "si":
            print("Permitir posicion de suficiente ventilación.")
            print("Fin.")
            return
        elif respira.lower() == "no":
            print("Administrar 5 ventilaciones y llamar a la ambulancia.")

            ambulancia = "no"
            while ambulancia == "no":
                signos = input("- ¿Signos de vida? (si/no): ")
                if signos.lower() == "no":
                    print("Administrar compresiones torácicas hasta que llegue la ambulancia.")
                    ambulancia = input("- ¿Llegó la ambulancia? (si/no): ")
                    if ambulancia.lower() == "si":
                        print("Fin")
                        return
                    elif ambulancia.lower() == "no":
                        continue  # Signos?
                    else:
                        print("Por favor escriba [si/no]")

                elif signos.lower() == "si":
                    print("Evaluar la espera de la ambulancia:")

                    ambulancia = input("- ¿Llegó la ambulancia? (si/no): ")
                    if ambulancia.lower() == "si":
                        print("Fin")
                        return

                    elif ambulancia.lower() == "no":
                        continue  # signos?
                    else:
                        print("Por favor escriba [si/no]")
                        
                else:   #Fin if signos
                    print("Por favor escriba [si/no]")
                #Fin while

        else: # fin if respira
            print("Por favor escriba [si/no]")


    else: # fin if 
        print("Por favor escriba [si/no]")



# Ejecutando la funcion principal
main()