
def normalize(nombre):

    a, b = 'áéíóúüñÁÉÍÓÚÜÑ', 'aeiouunAEIOUUN'
    trans = str.maketrans(a, b)

    return nombre.transtale(trans).lower().replace(" ","")
