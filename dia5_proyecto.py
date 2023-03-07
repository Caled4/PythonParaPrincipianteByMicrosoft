# El programa va a elegir una palabra secreta y le va a mostrar al jugador solamente una serie de guiones que representa la cantidad de letras que tiene la palabra.
# El jugador en cada turno deberá elegir una letra y si la letra se encuentra en la palabra oculta, el sistema le va a mostrar en qué lugares se encuentra.
# Pero si el jugador dice una letra que no se encuentra en la palabra oculta, en ese caso pierde una vida.
import random

def ahorcados():
    palabras=["hoja","cola","uva"]
    palabra=list(random.choice(palabras))
    oculta=[]
    adivina=[]

    for x in range(0,len(palabra)):
        adivina.append(f=input("ingresa numero"))
        match x:
            case 1:
                print("x is equal to 1")
            case 2:
                print("x is equal to 2")
            case _:
                print("x is not equal to 1 or 2")
        oculta.append("*")
    print(palabra)
    print(oculta)
    print(adivina)
print(ahorcados())