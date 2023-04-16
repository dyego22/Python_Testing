#Docstring
#__doc__
def palindromo(sentence:str)-> bool:
    """Permite conocer si un string es o no palindromo.
    Args:
        sentence:string
    Returns:
        bool
    """

    sentence = sentence.lower().replace(' ','')
    return sentence == sentence[::-1]

print(palindromo.__doc__) #forma1
print(help(palindromo))#forma2