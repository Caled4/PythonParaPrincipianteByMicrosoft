# Este programa debería comenzar preguntando cosas al usuario, por lo tanto, vas a necesitar input parapoder recibir los ingresos del usuario y deberías usar variables para almacenar esos ingresos.
# Recuerda que los ingresos de usuarios se almacenan como strings.
# Por lo tanto, deberías convertir uno de esos ingresos en un float para poder hacer operaciones con él.
# Y qué operaciones necesitas hacer?Bueno, calcular el 13% del número que haya ingresado el usuario.Es decir, que debes multiplicar ese número por 13 y luego dividirlo por 100.Recuerda almacenar ese resultado en una variable.
# Sería bueno que para imprimir en pantalla el resultado te asegures de que esa información no tenga más de dos decimales.
nombre = input("Por favor, dime tu nombre: ")
ventas = int(input("Diga sus ventas totales del mes: "))

comision = round(ventas * 13 / 100,2)

print(f"Hola {nombre}, tus comisiones de este mes son de ${comision}")