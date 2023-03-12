# Y hoy vas a crear por primera vez un juego completamente funcional con el que podrás divertirte tú mismoun rato.
# La consigna es esta El programa le va a preguntar al usuario su nombre y luego le va a decir algo así como Bueno, Juan, he pensado un número entre el uno y el 100 y tienes solo ocho intentos para adivinar cuál crees que es el número.
# Entonces, en cada intento el jugador dirá un número y el programa puede responder cuatro cosas distintas.
# Si el número que dijo el usuario es menor a uno o superior a 100, le va a decir que elegir un número que no está permitido o algo así.
# Si el número que ha elegido el usuario es menor al que ha pensado el programa, le va a decir que su respuesta es incorrecta y que ha elegido un número menor al número secreto.
# Si el usuario eligió un número mayor al número secreto, bueno, también se lo hará saber de la misma manera.
# Y si el usuario acertó el número secreto, se le va a informar que ha ganado y cuántos intentos le ha tomado.
# Si el usuario no ha acertado en este primer intento, se le va a volver a pedir que elija otro número.
# Y así hasta que gane o hasta que se agoten los ocho intentos.

from random import randint

intentos = 0
estimado = 0
numero_secreto = randint(1,100)
nombre = input("Dime tu nombre: ")

print(f"Bueno {nombre}, he pensado un número entre 1 y 100\nTienes 8 intentos para adivinar")

while intentos < 8:
    estimado = int(input("Cuál es el número?: "))
    intentos += 1

    if estimado < numero_secreto:
        print("Mi numero es mas alto")
    elif estimado > numero_secreto:
        print("Mi numero es mas bajo")
    else:
        print(f"Felicitaciones {nombre}! Has adivinado en {intentos} intentos")
        break

if estimado != numero_secreto:
    print(f"Lo siento, se han agotado los intentos. El numero secreto era {numero_secreto}")