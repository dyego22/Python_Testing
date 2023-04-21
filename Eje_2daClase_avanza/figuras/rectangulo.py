import validaciones as val
def area_rectangulo():
    try:
        base = val.validar_numero_float(input('>>>>Ingrese la Medida de la Base: '))
        altura = val.validar_numero_float(input('>>>Ingrese la medida de la Altura: '))
        return (base*altura)
    except:
        print('Error: Debe ingresar un numero')
    