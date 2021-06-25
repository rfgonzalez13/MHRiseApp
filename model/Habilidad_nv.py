# coding = utf-8
from google.appengine.ext import ndb


class Habilidad_nv(ndb.Model):
    nivel = ndb.IntegerProperty(required=True, indexed=True)
    descripcion = ndb.TextProperty(required=True)


