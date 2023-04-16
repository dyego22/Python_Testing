#Doctest
#__doc__
import doctest
def palindromo(sentence:str)-> bool:
    """Permite saber si una string es o no palindromo

    Args:
        sentence (str): string a verificar

    Returns:
        bool: Devuelve True or False

    Example:
    >>> palindromo('anita lava la tina')
    True
    """    
    sentence = sentence.lower().replace(' ','')
    return sentence == sentence[::-1]

if __name__ == "__main__":
    import doctest
    doctest.testmod()