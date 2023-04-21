def validar_opcion(numero:str)->int:
    opcion = int(numero)
    if opcion > 0 and opcion <= 3:
        return opcion
    else: 
        raise Exception

def validar_numero_float(valor:str)->bool:
    numero = float(valor)
    if  type(numero) == float:
        return numero
    else:
        raise Exception
