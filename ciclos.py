###################
# bucles, loops o ciclos es estructura de control en programacion que permite ejecutar una o varias lines de codigo multiples veces


# for - se usa cuando sabemos cuantas veces se debe de repetir ciertas instrucciones
# i es una variable de control, esta se actualiza automaticamente antes de cada iteracion
#start para inicializar la variable, stop para detenerla y step para cuanto se le va a sumar
for i in range(5):
    print(i)

for n in range(5, 100, 5): #start, stop, step
    print(n)


#Ciclos iterables, que iteran sobre string, listas, tuplas, diccionarios, etc
for name in "Josafath":
    print(name)


for num in [1,2,3,4,5]:
    print(num)


player = {"n":2, "m":4, "b":5, "j":6, "p":11, "a":72}

for n in player:
    print(n)

for j in player.values():
    print(j)


for n, j in player.items():
    print(n,j)