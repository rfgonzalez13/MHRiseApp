# coding = utf-8
from google.appengine.ext import ndb


class Habilidades_pieza(ndb.Model):
    pieza = ndb.IntegerProperty(required=True, indexed=True)
    habilidad = ndb.IntegerProperty(required=True, indexed=True)
    nivel = ndb.IntegerProperty(required=True, indexed=True)
