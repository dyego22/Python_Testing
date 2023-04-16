#assert

if __name__ == '__main__':
    try:
        assert 5 == 10,'lo sentimos 5 no es igual a 10'
        print('>>> El Programa se ejecuta perfectamente')
    except AssertionError as error:
        print (error)