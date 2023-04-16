#Doctest
"""Documentando el modulo
"""
import doctest
class user:
    """permite obtener dator de los usuarios
    """
def __init__(self,username: str, password:str)-> None:
    """permite instanciar los objetos de tipo user

    Args:
        username (str): el username del usuario
        password (str): el password del usuario
    """
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    help(user())