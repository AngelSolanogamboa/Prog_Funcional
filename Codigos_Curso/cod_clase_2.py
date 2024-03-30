man_a = open('archivo.txt')
for linea in man_a:
    palabras = linea.split()
    print ("Depuracion: ",palabras)
    if len(palabras)==0 | palabras[0]!="From": continue 
    print(palabras [2])

def manejador(abrirArchivo):
    return open(abrirArchivo)

def barrido(manejador,NoLineas):
    
    return 

def noLineas(manejador):
    return manejador.length()

def filtrarFrom(linea):
    return linea.rstrip().startswith('From') 