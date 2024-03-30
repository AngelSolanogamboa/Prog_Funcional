
def abrirArchivo(archivo):
    return open(archivo)

def filtrarFrom(linea):
    return linea.rstrip().startswith('From') 

def map(linea):
    return linea.split()[2]

print(map(filter(filtrarFrom,abrirArchivo(input("ingrese el nombre del archivo")))))


# man_a = open('archivo.txt')
# for linea in man_a:
#     linea =linea.rstrip() # elimina los espacios bacios en los extrmos de la linea 
#     if not linea.startswith('From '): continue
#     palabras = linea.split()
#     print(palabras[2])

man_a = open('archivo.txt')
for linea in man_a:
    palabras = linea.split()
    print ("Depuracion: ",palabras)
    if palabras[0]!="From" | len(palabras)==0: continue 
    print(palabras [2])