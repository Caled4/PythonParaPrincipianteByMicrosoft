# Práctica Método Index() 1
# Encuentra y muestra en pantalla qué caracter ocupa la quinta posición dentro de la siguiente palabra: "ordenador"
# ----------------------------------------------------------------------------------------
palabra = "ordenador"
print(palabra[4])
# ----------------------------------------------------------------------------------------
# Práctica Método Index() 2
# Encuentra y muestra en pantalla el índice de la primera aparición de la palabra "práctica" en la siguiente frase:
# "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
# ----------------------------------------------------------------------------------------
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.index('práctica'))
# ----------------------------------------------------------------------------------------
# Práctica Método Index() 3
# Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" en la siguiente frase:
# "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
# ----------------------------------------------------------------------------------------
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.rindex('práctica'))
# ----------------------------------------------------------------------------------------
# Práctica Sub-Strings 1
# Extrae la primera palabra de la siguiente frase utilizando slicing, y muéstrala en pantalla:
# "Controlar la complejidad es la esencia de la programación"
# ----------------------------------------------------------------------------------------
frase = "Controlar la complejidad es la esencia de la programación"
print(frase[0:9])
# ----------------------------------------------------------------------------------------
# Práctica Sub-Strings 2
# Toma cada tercer car
# acter empezando desde el noveno hasta el final de la frase, e imprime el resultado.
# "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
# ----------------------------------------------------------------------------------------
frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
print(frase[8::3])
# ----------------------------------------------------------------------------------------
# Práctica Sub-Strings 3
# Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado en pantalla.
# "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
# ----------------------------------------------------------------------------------------
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
print(frase[-1::-1])
# ----------------------------------------------------------------------------------------
# Práctica Métodos de String 1
# Imprime el siguiente texto en mayúsculas, empleando el método específico de strings:
# ----------------------------------------------------------------------------------------
frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
print(frase.upper())
# ----------------------------------------------------------------------------------------
# Práctica Métodos de String 2
# Une la siguiente lista en un string, separando cada elemento con un espacio. Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado.
# ----------------------------------------------------------------------------------------
lista_palabras = ["La","legibilidad","cuenta."]
print(" ".join(lista_palabras))
# ----------------------------------------------------------------------------------------
# Práctica Métodos de String 3
# Reemplaza en la siguiente frase:
# "Si la implementación es difícil de explicar, puede que sea una mala idea."
# los siguientes pares de palabras:
#     "difícil" --> "fácil"
#     "mala" --> "buena"
# y muestra en pantalla la frase con ambas palabras modificadas.
# ----------------------------------------------------------------------------------------
frase="Si la implementación es difícil de explicar, puede que sea una mala idea."
print(frase.replace("difícil","fácil").replace("mala","buena"))
# ----------------------------------------------------------------------------------------
# Práctica Propiedades de Strings 1
# Concatena 15 veces el texto "Repetición" y muestra el resultado en pantalla. Por suerte, conoces que los strings son multiplicables y puedes realizar esta actividad de forma simple y elegante.
# ----------------------------------------------------------------------------------------
print("Repetición"*15)
# ----------------------------------------------------------------------------------------
# Práctica Propiedades de Strings 2
# Verifica si la palabra "agua" no se encuentra en el siguiente haiku. Debes imprimir el booleano.
# Tierra mojada,
# mis recuerdos de viaje
# entre las lluvias
# ----------------------------------------------------------------------------------------
haiku='''Tierra mojada
mis recuerdos de viaje,
entre las lluvias'''
print("agua" not in haiku)
# ----------------------------------------------------------------------------------------
# Práctica Propiedades de Strings 3
# Muestra en pantalla el largo (en números de caracteres) de la palabra electroencefalografista.
# ----------------------------------------------------------------------------------------
print(len('electroencefalografista'))
# ----------------------------------------------------------------------------------------
# Práctica Listas 1
# Crea una lista con 5 elementos, dentro de la variable mi_lista. Puedes incluir strings, booleanos, números, etc.
# ----------------------------------------------------------------------------------------
mi_lista={2,5,8,3,7}
# ----------------------------------------------------------------------------------------
# Práctica Listas 2
# Agrega el elemento "motocicleta" a la siguiente lista de medios de transporte:
# medios_transporte = ["avión", "auto", "barco", "bicicleta"]
# No debes modificar la línea de código ya suministrada, sino que debes emplear el método apropiado de listas para añadir un nuevo elemento.
# ----------------------------------------------------------------------------------------
medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")
# ----------------------------------------------------------------------------------------
# Práctica Listas 3
# Utiliza el método pop() para quitar el tercer elemento de la siguiente lista llamada frutas, y almacénalo en una variable llamada eliminado. Utiliza métodos de listas sin alterar la línea de código ya suministrada.
#     manzana
#     banana
#     mango
#     cereza
#     sandía
# ----------------------------------------------------------------------------------------
frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado=frutas.pop(2)
# ----------------------------------------------------------------------------------------
# Práctica Diccionarios 1
# Crea un diccionario llamado mi_dic que almacene la siguiente información de una persona:
#     nombre: Karen
#     apellido: Jurgens
#     edad: 35
#     ocupacion: Periodista
# Los nombres de las claves y valores deben ser iguales a la consigna.
# ----------------------------------------------------------------------------------------
mi_dic={'nombre': "Karen",'apellido': "Jurgens",'edad': 35,'ocupacion': "Periodista"}
# ----------------------------------------------------------------------------------------
# Práctica Diccionarios 2
# Crea una función print que devuelva del segundo item de la lista llamada points2, dentro del siguiente diccionario.
# Si el valor 300 cambiara en el futuro, el código debería funcionar igual para devolver el valor que se encuentre en esa misma posición. Para ello, deberás hacer referencia a los nombres de las claves y/o índices según corresponda
# ----------------------------------------------------------------------------------------
mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(str(mi_dict["puntos"]["points2"][1]))
# ----------------------------------------------------------------------------------------
# Práctica Diccionarios 3
# Actualiza la información de nuestro diccionario llamado mi_dic  (reasignando nuevos valores a las claves según corresponda), y agrega una nueva clave llamada "pais" (sin tilde). Los nuevos datos son:
#     nombre: Karen
#     apellido: Jurgens
#     edad: 36
#     ocupacion: Editora
#     pais: Colombia
# para ello, no debes cambiar la línea de código ya escrita, sino actualizar los valores mediante métodos de diccionarios.
# ----------------------------------------------------------------------------------------
mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic['pais']="Colombia"
mi_dic['edad']=36
mi_dic['ocupacion']="Editora"
# ----------------------------------------------------------------------------------------
# Práctica Tuples 1
# Utiliza un método de tuplas para contar la cantidad de veces que aparece el valor 2 en la siguiente tupla, y muestra el resultado (integer) en pantalla:
# mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
# ----------------------------------------------------------------------------------------
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))
# ----------------------------------------------------------------------------------------
# Práctica Tuples 2
# Convierte a lista la siguiente tupla, y almacénala en una variable llamada mi_lista.
# mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
# ----------------------------------------------------------------------------------------
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista=list(mi_tupla)
# ----------------------------------------------------------------------------------------
# Práctica Tuples 3
# Extrae los elementos de la siguiente tupla en cuatro variables: a, b, c, d
# mi_tupla = (1, 2, 3, 4)
# ----------------------------------------------------------------------------------------
mi_tupla = (1, 2, 3, 4)
a,b,c,d=mi_tupla
# ----------------------------------------------------------------------------------------
# Práctica Sets 1
# Une los siguientes sets en uno solo, llamado mi_set_3:
# {1, 2, "tres", "cuatro"}
# {"tres", 4, 5}
# ----------------------------------------------------------------------------------------
mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}
mi_set_3=mi_set_1.union(mi_set_2)
# ----------------------------------------------------------------------------------------
# Práctica Sets 2
# Elimina un elemento al azar del siguiente set, utilizando métodos de sets.
#     sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
# ----------------------------------------------------------------------------------------
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.remove("Camila")
# ----------------------------------------------------------------------------------------
# Práctica Sets 3
# Agrega el nombre Damián al siguiente set, utilizando métodos de sets:
# sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
# # ----------------------------------------------------------------------------------------
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add("Damián")
# ----------------------------------------------------------------------------------------
# Práctica Booleanos 1
# Realiza una comparación que arroje como resultado un booleano y almacena el resultado (True/False) en una variable llamada prueba
# ----------------------------------------------------------------------------------------
prueba=5>2
# ----------------------------------------------------------------------------------------
# Práctica Booleanos 2
# Verifica si 17834/34 es mayor que 87*56 y muestra el resultado (booleano) en pantalla utilizando print()
# ----------------------------------------------------------------------------------------
print(17834/34>87*56)
# ----------------------------------------------------------------------------------------
# Práctica Booleanos 3
# Verifica si la raíz cuadrada de 25 es igual a 5 y muestra el resultado (booleano) en pantalla utilizando print()
# ----------------------------------------------------------------------------------------
print(25*0.5!=5)
# ----------------------------------------------------------------------------------------