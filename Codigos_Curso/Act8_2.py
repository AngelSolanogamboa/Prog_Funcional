from functools import reduce 
def abrirArchivo(archivo):
    try:
        return open(archivo)
    except: 
        print("el arecibo no se puede abrir ",archivo)
        exit 

def filtrarFrom(linea):
    return linea.rstrip().startswith('From')

def obtener_tercera_palabra(linea):
    return linea.split()[1]

def lineas_filtradas():
    return filter(filtrarFrom, abrirArchivo(input("Ingrese el nombre del archivo: ")))

def terceras_palabras():
    return map(obtener_tercera_palabra, lineas_filtradas())

def  contar_palbras(counts,tercerasPalabras):
    return {**counts,tercerasPalabras:counts.get(tercerasPalabras,0)+1}

print(reduce(contar_palbras,terceras_palabras(),{}))