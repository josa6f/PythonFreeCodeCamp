########################
#una funcion es un bloque de codigo reutilizable que realiza una sola tarea especifica
#a function is a reusable block of code that performs a sigle specific task

def saludar():
    print("Hola!!")


saludar()
saludar()

#Parametro - variable que se incluye en la definicion de la funcion
#Parameter - varible to be included in the fuction definicion

def alumno(calificacion):
    if calificacion < 5:
        print("reprobado")
    else:
        print("aprovado")


alumno(7)
alumno(2)

def suma(x, y):
    print(x + y)


#argumento - valor que asignamos a un parametro cuando llamamos a una funcion 
#argument - value we assign to a parameter when calling a function

suma(6, 13)

#returnar un valor - regresar un calor despues completar la tarea
#return a value - return a value after completing the task

def multiplicacion(a, b):
    return(a * b)

print(multiplicacion(6, 13))