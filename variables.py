#Las variables se nombran con una letra num1 o con un guion -num1 y solo isan de a a Z y _

num1 = 500
num2 = 2000
suma = num1 + num2
print(suma)

#Typos de datos numerico

#enteros = positivos, negativos y 0
n = 2
print(type(n)) #para saber que tipo de dato <class 'int'>

#float = positivos, negativos y 0.01 (cero con decimales)
nfloat = 1.2
print(type(nfloat)) #<class 'float'>

#boolean = True o False, son importantes pra condicionales y loops
valor1 = True
print(type(valor1)) #<class 'bool'>

#Cadena de caracteres
cadena1 = "Josafath"
cadena2 = "Maria"

print(type(cadena1)) #<class 'str'>
print(len(cadena1)) #len es para la longitud del string
print(len(cadena2)) 

#Indexacion en el string

print(cadena1[0]) #Para ingresar a un valor de la cadena se utiliza la indexacion
print(cadena1[1])
print(cadena1[2])
print(cadena1[3])

#Rebanado o slicing, cuando ingresas a una parte de la cdena
print(cadena1[1:7]) #del caracter 1 al 6
print(cadena1[4:]) #del caracter 4 al fin
print(cadena1[:5]) #del inicio al 4
print(cadena1[:]) #duplicar todo el string

#Saltar
print(cadena1[1:8:2]) #del caracter 1 al 7, y saltando de 2, ejemplo inicia en 1, 1 + 2 = 3, el siguiente salto seria 3 despues 5,7