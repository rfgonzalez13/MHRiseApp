# coding = utf-8
from google.appengine.ext import ndb


class Armadura(ndb.Model):
    nombre = ndb.StringProperty(required=True, indexed=True)
    pk_nombre = ndb.StringProperty(required=True, indexed=True)
    casco = ndb.IntegerProperty(indexed=True)
    cota = ndb.IntegerProperty(indexed=True)
    brazales = ndb.IntegerProperty(indexed=True)
    faja = ndb.IntegerProperty(indexed=True)
    grebas = ndb.IntegerProperty(indexed=True)
