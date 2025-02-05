##abrir un archivo txt, que r es para leer y archivo es la variable a la que se le asigno el texto del archivo
# r - read
# w - write
# a - append
# add + read = w+ write and read

with open("josa.txt", "r") as archivo:
    print(archivo)



with open("josa.txt", "a") as archivo:
    archivo.write("Public 187.18.1.54\n")
