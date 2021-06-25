# coding=utf-8
# coding = utf-8
import time

import webapp2

from google.appengine.ext import ndb

from webapp2_extras import jinja2

from model.Habilidad import Habilidad

from model.Habilidad_nv import Habilidad_nv

from model.Habilidades_pieza import Habilidades_pieza

from google.appengine.api import users


class EliminarHabilidad(webapp2.RequestHandler):

    def get(self):

        msg = "Referencia a la habilidad perdida"
        link = "/panel_habilidades"

        try:
            id = self.request.get('id')
        except:
            return self.redirect("/error?edMsg=" + msg + "&edLink=" + link)

        msg = "Habilidad no encontrada"
        try:
            clave = ndb.Key(urlsafe=id)

            habilidad_nv = Habilidad_nv.query(ancestor=clave).order(Habilidad_nv.nivel)

        except:
            return self.redirect("/error?edMsg=" + msg + "&edLink=" + link)

        habilidades_pieza = Habilidades_pieza.query(Habilidades_pieza.habilidad == clave.id())

        for hab_p in habilidades_pieza:
            hab_p.key.delete()

        for hab_nv in habilidad_nv:
            hab_nv.key.delete()

        clave.delete()
        time.sleep(1)
        return self.redirect("/panel_habilidades")


app = webapp2.WSGIApplication([
    ('/habilidades/eliminar', EliminarHabilidad)
], debug=True)
