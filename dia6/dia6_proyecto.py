# Tu código le va a dar primero la bienvenida al usuario.
# Le voy a informar la ruta de acceso al directorio donde se encuentra nuestra carpeta de recetas.
# Le voy a informar cuántas recetas hay en total dentro de esa carpeta y luego le voy a pedir que elija una de estas opciones que tenemos aquí.
# La primera opción le va a preguntar qué categoría elige carnes, ensaladas, etcétera Y una vez que el usuario elija una, le va a preguntar qué receta quiere leer y mostrar su contenido.
# En la opción número dos también se le va a hacer elegir una categoría, pero luego le va a pedir que escriba el nombre y el contenido de la nueva receta que quiere crear y el programa va a crear ese archivo en el lugar correcto.
# La opción número tres le va a preguntar el nombre de la categoría que quiere crear y va a generar una carpeta nueva con ese nombre.
# Luego viene la opción cuatro, que hará todo lo mismo que la opción uno, pero en vez de leer la receta la ve eliminar
#  la opción cinco, que es la penúltima Le va a preguntar qué categoría quiere eliminar y finalmente la opción seis, que simplemente va a finalizar la ejecución del código.
# ----------------------------------------------------------------------------------------
import os
import shutil
import sys
def categoria():
    # mostrar menu
    lista_categoria=[ lista_categoria for lista_categoria in os.listdir("Recetas") ]
    print("\n".join(map(str, enumerate(lista_categoria))))
    opcion_categoria=int(input("ingrese el numero de su seleccion: "))
    os.system('cls')
    # mostrarplatos
    if opcion_categoria>=0 and opcion_categoria<=3:
        lista_platos=[lista_platos for lista_platos in os.listdir(f"Recetas\\{lista_categoria[opcion_categoria]}")]
        print("\n".join(map(str,enumerate(lista_platos))))
    else:
        print("Tu opcion es INVALIDA como TU")
    # seleccionar plato
    opcion_plato=int(input("Ingresa el numero de su seleccion: "))
    ruta_plato=f"Recetas\\{lista_categoria[opcion_categoria]}\\{lista_platos[opcion_plato]}"
    os.system('cls')
    print(lista_platos[opcion_plato])
    # mostrar opciones de acciones
    print("1 leer receta\t\t2 crear receta\n3 crear categoria\t4 eliminar receta\n5 eliminar categoria\t6 salir del programa")
    opcion_accion=int(input("Ingresa el numero de su seleccion: "))
    match opcion_accion:
        case 1:
            os.system("cls")
            with open(ruta_plato, "r") as plato:
                plato = plato.read()
                print(plato)
        case 2:
            nombre_plato=input("ingresa el nombre de tu receta: ")
            contenido_receta=input("Escribe tu receta")
            with open(nombre_plato+".txt","w") as nueva_raceta:
                nueva_raceta.write(contenido_receta)
        case 3:
            nueva_categoria=input("Escribe la nueva categoria: ")
            os.mkdir("Recetas\\"+nueva_categoria)
        case 4 :
            os.remove("Recetas\\"+lista_categoria[opcion_categoria]+"\\"+lista_platos[opcion_plato])
        case 5 :
            shutil.rmtree(r"Recetas\{lista_categoria[opcion_categoria]}")
        case 6:
            sys.exit()
        case _ :
            print("Tu opcion es INVALIDA como TU")

categoria()
