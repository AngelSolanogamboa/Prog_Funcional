def chicles():
    return int(input("ingrese la cantidad: ")) * 0.8

def cerillos():
    return int(input("ingrese la cantidad: ")) * 1.26

def javon():
    return int(input("ingrese la cantidad: ")) * 18.45

def subtotal ():
    return float(chicles()+cerillos()+javon())

def total2():  
     return float(subtotal() * 1.16)
     
print(round(total2()))