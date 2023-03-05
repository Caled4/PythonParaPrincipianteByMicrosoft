# La consigna es la siguiente Vas a crear un programa que primero le pida al usuario que ingrese un texto?
# Puede ser un texto cualquiera o un artículo entero, un párrafo, una frase, un poema, lo que quiera.
# Luego el programa le va a pedir al usuario que también ingrese tres letras a su elección y a partir de ese momento nuestro código va a procesar esa información para hacer cinco tipos de análisis y lo que va a hacer es devolverle al usuario la siguiente información Primero, cuantas veces aparece cada una de las letras que eligió?
# Para lograr esto te recomiendo almacenar esas letras en una lista y luego usar algún método propio de string que nos permita contar cuantas veces aparece un sub string dentro del string.
# Algo que debes tener en cuenta es que al buscar las letras pueden haber mayúsculas y minúsculas y esto va a afectar el resultado.
# Pero lo que deberías hacer para asegurarte de que se encuentren absolutamente todas las letras es pasa tanto el texto original como las letras a buscar en minúsculas.
# Segundo, le vas a decir al usuario cuántas palabras hay a lo largo de todo el texto.
# Y para lograr esta parte, recuerda que hay un método de string que permite transformarlo en una lista y que luego hay una función que permite averiguar el largo de una lista.
# Tercero, nos va a informar cuál es la primera letra del texto y cuál es la última.
# Aquí claramente echaremos mano de la indexación cuando el sistema nos va a mostrar cómo quedaría el texto si invirtiéramos el orden de las palabras.
# Acaso hay algún método que permita invertir el orden de una lista y otro que permita unir esos elementos con espacios intermedios? Piénsalo.
# Y por último, el sistema nos va a decir si la palabra python se encuentra dentro del texto.
texto = input("Ingresa un texto a elección: ")
letras = []

texto = texto.lower()

letras.append(input("Ingresa la primera letra: ".lower()))
letras.append(input("Ingresa la segunda letra: ".lower()))
letras.append(input("Ingresa la tercera letra: ".lower()))

print("\n")
print("CANTIDAD DE LETRAS")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces")

print("\n")
print("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en tu texto")

print("\n")
print("LETRAS DE INICIO Y DE FIN")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"La letra inicial es '{letra_inicio}' y la letra final es '{letra_final}'")

print("\n")
print("TEXTO INVERTIDO")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Si ordenamos tu texto al revés va a decir: '{texto_invertido}'")

print("\n")
print("BUSCANDO LA PALABRA PYTHON")
buscar_python = 'python' in texto
dic = {True:"sí", False:"no"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")