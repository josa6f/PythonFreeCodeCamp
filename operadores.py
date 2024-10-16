#exprecion es cuando se evaluan valores, variables y operadores para que resulte un valor

#Operadores aritmeticos permiten, suma, resta, multiplicacion, division, division entera, exponente, modulo

#orden de las operaciones Parentesis, Exponentes, Multiplicacion, division, suma y resta

suma = 5 + 10
print(suma)

resta = 5 - 10
print(resta)

multiplicacion = 5 * 10
print(multiplicacion)

division = 10 / 2 #Se obtiene un numero float
print(division)

divisionEntera = 15 // 5 #con // se optiene un numero entero
print(divisionEntera)

exponente = 2 ** 7 
print(exponente)

modulo = 30 % 11  #retorna lo que resta de la division
print(modulo)


#########################
#Operadores Logicos, nos permiten trabajar con valores booleanos (and - los dos tienen que ser verdaderos, or - una debe de ser verdadera, not - niega la expresion dada)
#la prioridad es NOT, AND y OR

# AND

num1 = 10
num2 = 20
num3 = 30
if num1 < num2 and num2 < num3:
    print("Las dos operaciones son verdedareas")
else:
    print("uno de los dos es falso")


#Or
if num1 > num2 or num2 < num3:
    print("Se cumplio una de las dos operaciones")
else:
    print("los dos son falsos")

#NOT


############################
#Operadores relacionales - Se utilizan para comparar valores y retornan un valor booleano > - mayor que >= - mayor o igual que < - menor que <= - menor o igual que == - igual a  != - desigual a- 

igual = num1 == num1
print(igual)

desigual = num1 != num2
print(desigual)

menorQue = "a" < "b"
print(menorQue) 

mayorQue = "z" > "c"
print(mayorQue)

###############################
#Operadores de asignacion - nos permiten asignar valores a las variables del programa - = += -= *= /= **= //= %=

print(num1) # imprime 10
num1 += 5   # se llama a la variable num1 que es = 10 y se le suma y se le suma 5 y se le asigna a la variable
print(num1) # ahora la variable tiene 15

print(num1) 
num1 -= 10   #ahora se le resta 10
print(num1) 

num4 = 6
num4 %= 2
print(num4)