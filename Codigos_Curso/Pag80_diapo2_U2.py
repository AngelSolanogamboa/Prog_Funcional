from functools import reduce 
import string

def ordena(diccionario):
    return sorted(list(diccionario.items()),key=lambda x:x[1],reverse=True)[:10]
    
def imprime(diccionario):
    return list(map(lambda x:print(x),ordena(diccionario)))
    
def limpiar_texto(linea):
      return linea.translate(linea.maketrans('','',string.punctuation)).lower()
    
def lista_palabras(texto):
    return limpiar_texto(texto.strip()).split()
    
def contar_palabras(count,palabra):
    return {**count,palabra:count.get(palabra,0)+1} 
    
def linea_texto(contador,texto):
    return reduce(contar_palabras,lista_palabras(texto),contador)
    
imprime(reduce(linea_texto,open(input("ingresa el nombre del archivo: ")),{}))