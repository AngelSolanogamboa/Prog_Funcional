from functools import reduce 

#paradigma imperativo 
palabra = "brontosaurio"
d=dict()
for c in palabra:
    d[c]=d.get(c,0)+1
print(d)
        
print()

#paradigma funcional
def actualizar_diccionario(diccionario,letra):
    return {**diccionario, letra: diccionario.get(letra,0)+1}
print(reduce(actualizar_diccionario,"brontosaurio",{}))