# El programa va a elegir una palabra secreta y le va a mostrar al jugador solamente una serie de guiones que representa la cantidad de letras que tiene la palabra.
# El jugador en cada turno deberá elegir una letra y si la letra se encuentra en la palabra oculta, el sistema le va a mostrar en qué lugares se encuentra.
# Pero si el jugador dice una letra que no se encuentra en la palabra oculta, en ese caso pierde una vida.
import random

def ahorcados():
    palabras=["hojita","cola","uva"]
    palabra=list(random.choice(palabras))
    oculta=[]
    vida=len(palabra)
    print("ADIVINA LA PALABRA")
#imprimimos la palabra en *
    for i in range(0,len(palabra)):
        oculta.append("*")
    print(oculta)
#recoremos la palabra
    for x in range(0,len(palabra)):
#  pedimos que ingrese su letra
        letra=input(f"{vida} vidas, ingresa tu letra: ").lower()
#validamos que letra este en la palabra
        if letra in palabra:
            a=palabra.index(letra)
            oculta[a]=letra
#mostramos en pantalla la palacon la letra
        print(oculta)
#reducimos vida por intento
        vida-=1
    if "*" in oculta:
        print("PERDISTE")
    else:
        print("EN HORA BUENA HAS GANADO")
ahorcados()