# Actividad 4
def cantidad():
    return float(input("ingrese la cantidad: "))
 
def multiplicacion(cant,presio):
    return float(cant * presio)

def subTotal ():
     return multiplicacion(cantidad(),0.8) + multiplicacion(cantidad(),1.26) + multiplicacion(cantidad(),18.45)

def  iva(subtotal):
    return multiplicacion(subtotal,0.16)

def total(subtotal):
    print("Costo total: ") 
    return subtotal + iva(subtotal)

print(round(total(subTotal())))





