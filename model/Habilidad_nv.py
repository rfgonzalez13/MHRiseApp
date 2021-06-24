# coding = utf-8
from google.appengine.ext import ndb

from Habilidad import Habilidad


class Habilidad_nv(ndb.Model):
    habilidad = ndb.KeyProperty(kind=Habilidad, required=True)
    nivel = ndb.IntegerProperty(required=True, indexed=True)
    descripcion = ndb.TextProperty(required=True)


@ndb.transactional
def update(habilidad_nv):
    return habilidad_nv.put()
