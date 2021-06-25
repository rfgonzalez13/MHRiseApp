# coding=utf-8
# coding = utf-8
import time

import webapp2

from google.appengine.ext import ndb

from webapp2_extras import jinja2

from model.Armadura import Armadura

from model.Habilidades_pieza import Habilidades_pieza

from model.Pieza import Pieza


class EliminarArmadura(webapp2.RequestHandler):

    def get(self):

        msg = "Referencia a la armadura perdida"
        link = "/panel_armaduras"

        try:
            id = self.request.get('id')
        except:
            return self.redirect("/error?edMsg=" + msg + "&edLink=" + link)

        msg = "Armadura no encontrada"
        try:
            clave_armadura = ndb.Key(urlsafe=id)
            armadura = clave_armadura.get()
        except:
            return self.redirect("/error?edMsg=" + msg + "&edLink=" + link)

        if armadura.casco is not None:
            casco = Pieza.get_by_id(armadura.casco)
            casco.key.delete()
            habilidades_pieza = Habilidades_pieza.query(Habilidades_pieza.pieza == armadura.casco)
            for hab_p in habilidades_pieza:
                hab_p.key.delete()

        if armadura.cota is not None:
            cota = Pieza.get_by_id(armadura.cota)
            cota.key.delete()
            habilidades_pieza = Habilidades_pieza.query(Habilidades_pieza.pieza == armadura.cota)
            for hab_p in habilidades_pieza:
                hab_p.key.delete()

        if armadura.brazales is not None:
            brazales = Pieza.get_by_id(armadura.brazales)
            brazales.key.delete()
            habilidades_pieza = Habilidades_pieza.query(Habilidades_pieza.pieza == armadura.brazales)
            for hab_p in habilidades_pieza:
                hab_p.key.delete()

        if armadura.faja is not None:
            faja = Pieza.get_by_id(armadura.faja)
            faja.key.delete()
            habilidades_pieza = Habilidades_pieza.query(Habilidades_pieza.pieza == armadura.faja)
            for hab_p in habilidades_pieza:
                hab_p.key.delete()

        if armadura.grebas is not None:
            grebas = Pieza.get_by_id(armadura.grebas)
            grebas.key.delete()
            habilidades_pieza = Habilidades_pieza.query(Habilidades_pieza.pieza == armadura.grebas)
            for hab_p in habilidades_pieza:
                hab_p.key.delete()

        clave_armadura.delete()

        time.sleep(1)
        return self.redirect("/panel_armaduras")


app = webapp2.WSGIApplication([
    ('/armaduras/eliminar', EliminarArmadura)
], debug=True)
