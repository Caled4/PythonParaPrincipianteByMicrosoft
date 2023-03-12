#EJERCICO 1
# Crea una función llamada devolver_distintos() que reciba 3 integers como parámetros.
# Si la suma de los 3 numeros es mayor a 15, va a devolver el número mayor.
# Si la suma de los 3 numeros es menor a 10, va a devolver el número menor.
# Si la suma de los 3 números es un valor entre 10 y 15 (incluidos) va a devolver el número de valor intermedio.
# ---------------------------------------------------------------------------------------
def devolver_deistintos(uno,dos,tres):
    suma=sorted([uno,dos,tres])
    if sum(suma)>15:
        return suma[2]
    elif sum(suma)<10:
        return suma[0]
    else:
        return suma[1]
# print(devolver_deistintos(3,1,1))
# ----------------------------------------------------------------------------------------
# EJERCICIO 2
# Escribe una función (puedes ponerle cualquier nombre que
# quieras) que reciba cualquier palabra como parámetro, y que
# devuelva todas sus letras únicas (sin repetir) pero en orden
# alfabético.
# Por ejemplo si al invocar esta función pasamos la palabra
# "entretenido", debería devolver ['d', 'e', 'i', 'n', 'o', 'r', 't']
# ----------------------------------------------------------------------------------------
def nombre_randon(palabra):
    return sorted(set(list(palabra)))

# print(nombre_randon("bruno"))
# ----------------------------------------------------------------------------------------
# EJERCICIO 3
# Escribe una función que requiera una cantidad indefinida de
# argumentos. Lo que hará esta función es devolver True si en
# algún momento se ha ingresado al numero cero repetido dos
# veces consecutivas.
# Por ejemplo:
# (5,6,1,0,0,9,3,5) >>> True
# (6,0,5,1,0,3,0,1) >>> False
# ----------------------------------------------------------------------------------------
def ejercicio3(*args):
    for x in range(0,len(args)):
       if args[x]==0 and args[x-1]==0:
           return True
    return False
# print(ejercicio3(4,5,6,0,8,0,0))
# ----------------------------------------------------------------------------------------
# EJERCICO 4
# Escribe una función llamada contar_primos() que requiera un
# solo argumento numérico.
# Esta función va a mostrar en pantalla
# todos los números
# primos existentes en el rango que va desde cero hasta ese
# número incluido, y va a devolver la cantidad de números
# primos que encontró.
# Aclaración, por convención el 0 y el 1 no se consideran primos.
def contar_primos(numero):
    contador=0
    for x in range(0,numero+1):
        if x %2==0:
            contador+=1
    return contador

# print(contar_primos(5))