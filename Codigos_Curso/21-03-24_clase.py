from functools import reduce 
#conjuntos

pares={2,4,6,8,10}
vacio={}
set("hola")

bebida={'martini':{'vodka','remouth'},'black rusian':{'vodka','kablus'},
        'white rusian':{'cram','kablus','vodka'},'manhattan':{'rye','vermouth','bittes'},
        'screwdriver':{'orange juile','vodka'}}

for bebidas,ingrediente in bebida.items():
    if 'vodka' in ingrediente:
        print(bebida)


def diccionario(): 
    return {'martini' : {'vodka', 'vermouth', 'aceituna'}, 
            'black russian' : {'cream', 'kahlva', 'vodka'},
            'mahattan' : {'rye', 'vermouth', 'butters'}, 
            'screwdriver' : {'orange juice', 'vodka'}, 
            'cosmopolitan' : {'vodka', 'triple sec', 'jugo de arandano', 'limon'}}

def cocteles_ingredientes(cocteles):
    return list(filter(lambda x: 'limon' in cocteles[x], cocteles))

print()
print(cocteles_ingredientes(diccionario()))


