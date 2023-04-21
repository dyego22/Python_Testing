from math import pi
import validaciones as val
def area_circulo():
    try:
        radio = val.validar_numero_float(input('>>>>Ingrese el radio del circulo: '))
        return round((pi * radio**2),2)
    except:
        print('>>>> Error debe ingresar un numero')
        
        