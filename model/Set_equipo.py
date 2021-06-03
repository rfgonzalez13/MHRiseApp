# coding = utf-8
from google.appengine.ext import ndb

from Armadura import Armadura

class Set_equipo(ndb.Model):
    nombre = ndb.StringProperty(required=True, indexed=True)
    usuario = user = ndb.StringProperty(required=True, indexed=True)
    fecha = ndb.DateProperty(auto_now_add=True)
    casco = ndb.keyProperty(key=Armadura)
    cota = ndb.keyProperty(key=Armadura)
    brazales = ndb.keyProperty(key=Armadura)
    faja = ndb.keyProperty(key=Armadura)
    grebas = ndb.keyProperty(key=Armadura)


@ndb.transactional
def update(set_equipo):
    return set_equipo.put()
