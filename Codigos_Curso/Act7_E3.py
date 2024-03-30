from functools import reduce

def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return archivo.readlines()

def dividir_en_palabras(linea):
    return linea.split()

def agregar_palabra(palabras_unicas, palabras):
    return palabras_unicas | set(palabras)

def procesar_palabras_unicas(nombre_archivo):
    lineas = leer_archivo(nombre_archivo)
    palabras_unicas = reduce(agregar_palabra, map(dividir_en_palabras, lineas), set())
    return sorted(palabras_unicas)

list(map(print, procesar_palabras_unicas("romeo.txt")))