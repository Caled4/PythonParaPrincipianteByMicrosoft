# Práctica Abrir y Manipular Archivos 1
# Abre el archivo texto.txt e imprime su contenido.
# Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código
# ----------------------------------------------------------------------------------------
# archivo = open("texto.txt", "r")
# contenido = archivo.read()
# print(contenido)
# archivo.close()
# ----------------------------------------------------------------------------------------
# Práctica Abrir y Manipular Archivos 2
# Imprime la primera línea del archivo texto.txt
# No olvides abrir el archivo y cerrarlo luego de ejecutar tu código.
# Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código
# ----------------------------------------------------------------------------------------
# archivo=open("texto.txt","r")
# contenido = archivo.readline()
# print(contenido)
# archivo.close()
# ----------------------------------------------------------------------------------------
# Práctica Abrir y Manipular Archivos 3
# Abre el archivo texto.txt e imprime únicamente la segunda línea.
# ----------------------------------------------------------------------------------------
# archivo=open("texto.txt","r")
# contenido = archivo.readline()
# contenido = archivo.readline()
# print(contenido)
# archivo.close()
# ----------------------------------------------------------------------------------------
# Práctica Crear y Escribir Archivos 1
# Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto".
# Imprime el contenido completo de "mi_archivo.txt" al finalizar.
# Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.
# ----------------------------------------------------------------------------------------
# archivo=open('texto.txt','w')
# contenido= archivo.write('Nuevo texto')
# archivo=open('texto.txt','r')
# contenido=archivo.read()
# print(contenido)
# archivo.close()
# ----------------------------------------------------------------------------------------
# Práctica Crear y Escribir Archivos 2
# Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: "Nuevo inicio de sesión".
# Imprime el contenido completo de "mi_archivo.txt" al finalizar.
# Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.
# ----------------------------------------------------------------------------------------
# with open("mi_archivo.txt", "a") as archivo:
#     archivo.write("Nuevo inicio de sesión\n")
# with open("mi_archivo.txt", "r") as archivo:
#     contenido = archivo.read()
# print(contenido)
# ----------------------------------------------------------------------------------------
# Práctica Crear y Escribir Archivos 3
# Utiliza el método writelines para escribir los valores de la siguiente lista al final del archivo "registro.txt" . Inserta un tabulador entre cada elemento de la lista para separarlos.
# registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
# Imprime el contenido completo de "registro.txt" al finalizar.
# ----------------------------------------------------------------------------------------
# archivo=open("texto.txt",'a')
# registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
# for n in range(0,len(registro_ultima_sesion)):
#     archivo.writelines("\t"+registro_ultima_sesion[n]+"\t")
#
# archivo.close()
# archivo=open("texto.txt","r")
# print(archivo.read())
# ----------------------------------------------------------------------------------------
# Práctica Path 1
# Almacena en la variable ruta_base, un objeto Path que señale el directorio base del usuario.
# ----------------------------------------------------------------------------------------
# from pathlib import Path
# ruta_base=Path.home()
# ----------------------------------------------------------------------------------------
# Práctica Path 2
# Implementa y crea una ruta relativa que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:
# ----------------------------------------------------------------------------------------
# from pathlib import Path
# ruta= Path("Curso Python","Día 6","practicas_path.py")
# ----------------------------------------------------------------------------------------
# Práctica Path 3
# Implementa y crea una ruta absoluta que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:
# Almacena el directorio obtenido en la variable ruta.
# ----------------------------------------------------------------------------------------
# from pathlib import Path
# ruta=Path(Path.home(),"Curso Python","Día 6","practicas_path.py")
# ----------------------------------------------------------------------------------------
# Práctica Archivos y Funciones 1
# Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, y devuelva su contenido (read).
# ----------------------------------------------------------------------------------------
# def abrir_leer(archivo):
#     with open(archivo,'r') as archivo:
#         return archivo.read()
# ----------------------------------------------------------------------------------------
# Práctica Archivos y Funciones 2
# Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro, y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"
# ----------------------------------------------------------------------------------------
# def sobrescribir(archivo):
#     with open(archivo,'w') as archivo:
#         archivo.write("contenido eliminado")
# ----------------------------------------------------------------------------------------
# Práctica Archivos y Funciones 3
# Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro, y lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución". Finalmente, debe cerrar el archivo abierto.
# ----------------------------------------------------------------------------------------
def registro_error(archivo):
    with open(archivo,'a') as archivo:
        return archivo.write("se ha registrado un error de ejecución")

