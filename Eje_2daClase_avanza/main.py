import validaciones as val
import figuras
while True:
    try: 
        opcion  = val.validar_opcion(input('''
        Seleccione una Opcion:
        1) Area de Rectangulo
        2) Area Circulo
        3) salir
        '''))
        if opcion == 1:
            print('Area Rectangulo')
            area = figuras.area_rectangulo()
        elif opcion == 2:
            print('Area Circulo')
            area = figuras.area_circulo()
        else:
            print('>>>>Hasta la Proxima')
            break
    except:
        print('>>>> Opcion no valida ')

    if area != None:
        print('El area de la figura es: ',area)
        area=None