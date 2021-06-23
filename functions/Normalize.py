# coding=utf-8
# coding utf-8


import unicodedata


def normalize(nombre):
    s = ''.join((c for c in unicodedata.normalize('NFD', unicode(nombre)) if unicodedata.category(c) != 'Mn'))
    return s.decode().lower().replace(" ", "")
