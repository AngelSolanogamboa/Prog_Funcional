from functools import reduce 
def menu():
    print("\nmenu de operaciones")
    print("1.Inventario inicial")
    print("2.Venta")
    print("3.Compra")
    return int(input("seleccione una accion, ingresando el numero de operacion: "))

def seleccionar_producto(diccionarioDB):
    print("1."+str(diccionarioDB[1]['producto']))
    print("2."+str(diccionarioDB[2]['producto']))
    print("3."+str(diccionarioDB[3]['producto']))
    return int(input("seleccione un producto, ingresando el nuero de producto: "))

def structuraDB():
    return {1:{'producto':nombre_producto(),'tabla':{'entradas':0,'salidas':0,'existencia':0,'unitario':0.0,'promedio':0.0,'debe':0,'haber':0,'saldos':0.0}},
            2:{'producto':nombre_producto(),'tabla':{'entradas':0,'salidas':0,'existencia':0,'unitario':0.0,'promedio':0.0,'debe':0,'haber':0,'saldos':0.0}},
            3:{'producto':nombre_producto(),'tabla':{'entradas':0,'salidas':0,'existencia':0,'unitario':0.0,'promedio':0.0,'debe':0,'haber':0,'saldos':0.0}}}

def nombre_producto():
    return input("ingrese el nombre del proucto: ")

def switch_case(diccionarioDB,case):
    return inventario_inicial(diccionarioDB,switch_case2(diccionarioDB,seleccionar_producto(diccionarioDB))) if case==1 else case2(diccionarioDB,case)

def case2(diccionarioDB,case):
    return venta(diccionarioDB,switch_case2(diccionarioDB,seleccionar_producto(diccionarioDB))) if  case==2 else  Compra(diccionarioDB,switch_case2(diccionarioDB,seleccionar_producto(diccionarioDB)))
   
def switch_case2(diccionarioDB,case):
    return {1:diccionarioDB.get(1),
            2:diccionarioDB.get(2),
            3:diccionarioDB.get(3)}.get(case),int(case)

def guardarCambios(clave,diccionario,dicnuev,numdic):
    return modificarStructuraDB(diccionario[clave],guradarTabla,dicnuev,numdic) if clave==numdic else diccionario[clave] 

def modificarStructuraDB(diccionario,funcion_modificadora,dicnuevo,numdic):
    return {clave: funcion_modificadora(clave,diccionario,dicnuevo,numdic) for clave  in diccionario}

def guradarTabla(clave,diccionario,dicnuevo,numdic):
    return dicnuevo if clave=='tabla' else diccionario[clave]

def print_return(diccionario):
    print(diccionario)
    return diccionario

def modificar_valores(diccionario, funcion_modificadora):
    return {clave: funcion_modificadora(clave,diccionario) for clave in diccionario}

#------------------------------------------------------------------------------------------------------------------------------------
def inventario_inicial(diccionarioDB,dic_producto):
    print("\nInventario inicial")
    switch_case(modificarStructuraDB(diccionarioDB,guardarCambios,print_return(modificar_valores(modificar_valores(dic_producto[0]['tabla'],entradas_II) ,existencia_II)),dic_producto[1]),menu())

def entradas_II(clave,diccionario):
    return int(input("ingrese las entradas: ")) if clave=='entradas' else unitario_II(clave,diccionario)

def unitario_II(clave,diccionario):
    return int(input("ingrese el costo unitario: ")) if clave=='unitario' else diccionario[clave] 

def existencia_II(clave,diccionario):
    return diccionario['entradas'] if clave=='existencia' else promedio_II(clave,diccionario)

def promedio_II(clave,diccionario):
    return float(diccionario['unitario']) if clave=='promedio' else debe_II(clave,diccionario)

def debe_II(clave,diccionario):
    return diccionario.get('unitario') * diccionario.get('entradas') if clave=='debe' else saldos_II(clave,diccionario)

def saldos_II(clave,diccionario):
    return diccionario.get('unitario') * diccionario.get('entradas') if clave=='saldos' else diccionario[clave] 
 
#------------------------------------------------------------------------------------------------------------------------------------
def Compra(diccionarioDB,dic_producto):
    print("\nCompra")
    switch_case(modificarStructuraDB(diccionarioDB,guardarCambios,print_return(modificar_valores(modificar_valores(modificar_valores(dic_producto[0]['tabla'],entradas_II) ,existencia_C),saldos_C)),dic_producto[1]),menu())
    
def existencia_C(clave,diccionario):
    return diccionario['entradas'] + diccionario[clave] if clave=='existencia' else debe_C(clave,diccionario)

def debe_C(clave,diccionario):
    return diccionario.get('unitario') * diccionario.get('entradas') if clave=='debe' else diccionario[clave]

def saldos_C(clave,diccionario):
    return diccionario['debe'] + diccionario[clave] if clave=='saldos' else promedio_C(clave,diccionario)

def promedio_C(clave,diccionario):
    return round((diccionario['debe'] + diccionario['saldos'])  /  diccionario['existencia'],2)   if clave=='promedio' else salidas_haber(clave,diccionario) 

def salidas_haber(clave,diccionario):
    return 0 if clave=='salidas' else 0 if clave=='haber' else diccionario[clave] 

#--------------------------------------------------------------------------------------------------------------------------------------
def venta(diccionarioDB,dic_producto):
    print("\nVenta")
    switch_case(modificarStructuraDB(diccionarioDB,guardarCambios,print_return(modificar_valores(modificar_valores(dic_producto[0]['tabla'],salidas_V) ,existencia_V)),dic_producto[1]),menu())

def salidas_V(clave,diccionario):
    return int(input("ingrese las salidas: ")) if clave=='salidas' else 0 if clave=='entradas' else diccionario[clave] 

def existencia_V(clave,diccionario):
    return diccionario[clave] - diccionario['salidas'] if clave=='existencia' else unitario_V(clave,diccionario)

def unitario_V(clave,diccionario):
    return diccionario['promedio'] if clave=='unitario' else  haber_V(clave,diccionario)

def haber_V(clave,diccionario):
    return diccionario['salidas'] * diccionario['promedio'] if clave=='haber' else saldos_V(clave,diccionario)

def saldos_V(clave,diccionario):
    return diccionario[clave] - (diccionario['salidas'] * diccionario['promedio']) if clave=='saldos' else 0 if clave=='debe' else diccionario[clave] 

switch_case(structuraDB(),menu())