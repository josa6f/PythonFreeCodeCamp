#Numero entero
numeroEntero = int(input("Por favor, ingresa un numero entero: "))
print(f"EL tipo de tu numero entero es: {type(numeroEntero)}")

#Numero float
numeroFloat = float(input("Por favor, ingrese un numero flotante: "))
print(f"El tipo de dato de tu numero flotante es: {type(numeroFloat)}")

#numero boleano o boolean
valorBool = bool(input("Por favor ingresa un valor boleano: "))
print(f"El valor boleano es de tipo: {type(valorBool)}")

#string
cadenaStr = input("Por favor ingresa una cadena de texto")
print(f"La cadena de texto es del tipo: {type(cadenaStr)}")

if len(cadenaStr) > 5:
    print("La cadena tiene mas de 5 caracteres")
else:
    print("la cadena tiene 5 caracteres o menos")


#Manipulacion de cadenas a mayuscula
cadenaMayuscula = cadenaStr.upper()
print(f"La cadena en mayusculas es: {cadenaMayuscula}")

#slicing
mensaje = "redesconfiablessegurasyescalables"
print(mensaje[5:15])

mensajeMayusculas = mensaje.upper()
print(f"Esta es la palabra en mayusculas seleccionada: {mensajeMayusculas[15:22]}")

#Slicing con numeros
numeros = [1,2,3,4,5,6,7,8,9]
print(numeros[2:7])
print(numeros[0:9:3])