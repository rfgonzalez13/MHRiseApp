# coding = utf-8
from google.appengine.ext import ndb

from Armadura import Armadura
from Habilidad import Habilidad

class Habilidades_pieza(ndb.Model):
    nombre_armadura = ndb.KeyProperty(kind=Armadura)
    nombre_habilidad = ndb.KeyProperty(kind=Habilidad)
    nivel_habilidad = ndb.IntegerProperty(required=True, indexed=True)


@ndb.transactional
def update(habilidades_pieza):
    return habilidades_pieza.put()
