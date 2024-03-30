from functools import reduce 
import string 

#paradigma imperativo 
fname=input("ingrese el nombre del archivo: ")
try:
    fhand=open(fname)
except: 
    print("el arecibo no se puede abrir ",fname)
    exit()
counts=dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans("","",string.punctuation)) 
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word]=1
        else:   
            counts[word] +=1
print(counts)             
             
#paradigma funcional 
def abrir(archivo):
    try:
        return open(archivo)
    except: 
        print("el arecibo no se puede abrir ",archivo)
        exit 
        
def limpiar_linea(line):  
    return line.translate(line.maketrans("","",string.punctuation)).lower() 
    
def  contar_palbras(counts,words):
    return {**counts,words:counts.get(words,0)+1}
          
def lista_linea(linea):
    return limpiar_linea(linea.strip()).split()

def leer_lineas(diccionario,linea):
    return reduce(contar_palbras,lista_linea(linea),diccionario)
       
print(reduce(leer_lineas,abrir(input("ingrese el nombre del archivo: ")),{}))