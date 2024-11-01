#Arreglos - estructura de datos utilizada para almacenar multiples valores en secuencia - estas pueden ser mutables (modificadas)

numeroJ = [1,2,5,6,7,8,10,15,55]

print(numeroJ)
print(numeroJ[3])

#Agregar un elemento al final de la lista
numeroJ.append(92)
print(numeroJ)

#Agregar un elemento en un indice
numeroJ.insert(2,3) #el indice 2 y elemento 3
print(numeroJ)

#Eliminar el primer valor encontrado en el arreglo
numeroJ.remove(3)
print(numeroJ)

#encontrar un elemento con el operador IN y regresa un valor booleano True o False
if 6 in numeroJ:
    print("si tengo ese numero")

#index - retorna el indice de la primera ocurrencia del elemento en la lista

print(numeroJ.index(6))

#Cambiar un elemento en un indice especifico - esto es posible porque los arrays son mutables
numeroJ[0] = 0 # en el indice 0 asignale el valor 0
print(numeroJ)


###################################
#metodos de las listas - .count(elemento) - cuantas veces se repite un elemento, .extend(array) - extender una lista agregando elementos de otra lista, .pop() - elimina y retorna un element de una lista, .reverse() - reversa el orden de una lista, .sort() - ordena la lista

print(numeroJ.pop())
print(numeroJ)

numeroJ.reverse()
print(numeroJ)

numeroJ.extend([4,5,11,72])
print(numeroJ)

numeroJ.sort()
print(numeroJ)


############################
#Tuples - Estructura de datos inmutable que contiene una secuencia ordenada de elementos

josa = (6, "Football", "Musica", "Computacion", "Tauromaquia")
print(josa)
print(josa[4])
print(josa.index("Musica"))
print(josa.count("Musica"))


###########################
#Diccionarios - relaciona dos valores en una misma estructura de datos (coleccion de clave valor), son unicas e inmutables
players = {"majo": 13, "josafath": 6, "baby": 5, "mr": 4, "pako": 11, "paz": 72}
print(players["pako"])
print(players["majo"])
print(players["josafath"])
print(players["baby"])
print(players["mr"])
print(players["paz"])

#con el metodo get
print(players.get("josafath"))

#agregar una clave valor
players["nenuco"] = 2
players["baby"] = 8

print(players)

#removerlos
del players["majo"]

print(players)

