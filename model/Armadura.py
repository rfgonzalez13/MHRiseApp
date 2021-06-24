# coding = utf-8
from google.appengine.ext import ndb


class Armadura(ndb.Model):
    nombre = ndb.StringProperty(required=True, indexed=True)
    pieza = ndb.StringProperty(required=True, indexed=True, choices=["Casco", "Cota", "Brazales", "Faja", "Grebas"])


