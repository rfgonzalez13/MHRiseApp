# coding = utf-8
from google.appengine.ext import ndb


class Pieza(ndb.Model):
    nombre = ndb.StringProperty(required=True, indexed=True)
    pieza = ndb.StringProperty(required=True, indexed=True, choices=["Casco", "Cota", "Brazales", "Faja", "Grebas"])
