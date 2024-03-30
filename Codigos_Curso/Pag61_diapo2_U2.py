from functools import reduce 

#paradigma imperativo 
palabra = "brontosaurio"
d=dict()
for c in palabra:
    if c not in d:
        d[c]=1
    else:
        d[c]=d[c]+1
print(d)
        
print()

#paradigma funcional
def actualizar_diccionario(diccionario,letra):
    return {**diccionario, letra: diccionario[letra]+1 if letra in diccionario else 1}
print(reduce(actualizar_diccionario,"brontosaurio",{}))