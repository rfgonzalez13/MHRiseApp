# coding = utf-8
from google.appengine.ext import ndb


class Habilidad(ndb.Model):
    nombre = ndb.StringProperty(required=True, indexed=True)
    nivel_max = ndb.IntegerProperty(required=True, indexed=False)
    descripcion = ndb.TextProperty(required=True)
    pk_nombre = ndb.StringProperty(required=True, indexed=True)


