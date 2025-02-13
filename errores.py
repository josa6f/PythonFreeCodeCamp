#Errores y Excepciones
#SyntaxError - error de indentacion
#IndicesError, keyError (cuando la clave no existe en un diccionario), NameError(cuando una variable no esta definida) - Excepciones

#try:
    #Intenta ejecutar este codigo
#except:
    #si ocurre una excepcion, detente inmediatamente y ejecuta este codigo

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

try:
    resultado = num1 / num2
    print(f"{num1} / {num2} =", resultado)
except ZeroDivisionError as e:
    print(e)
finally:
    print("finally")

