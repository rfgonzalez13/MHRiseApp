# coding=utf-8
# coding = utf-8

import time

import webapp2

from webapp2_extras import jinja2

from model.Set import Set

from google.appengine.api import users


class GuardarSet(webapp2.RequestHandler):

    def get(self):

        msg = "Usuario Logeado"
        link = "/panel_sets"

        return self.redirect("/error?edMsg=" + msg + "&edLink=" + link)

    def post(self):
        user = users.get_current_user()

        nombre = self.request.get("edNombre", "")

        msg = "No se ha encontrado un nombre para la armadura"
        link = "/panel_sets"

        if nombre.strip() == "":
            return self.redirect("/error?edMsg=" + msg + "&edLink=" + link)

        msg = "Usuario no encontrado"

        if user:
            set = Set(nombre=nombre, user=user.user_id())
            casco = self.request.get("edCasco", "")
            if casco != "":
                set.casco = int(casco)

            cota = self.request.get("edCota", "")
            if cota != "":
                set.cota = int(cota)

            brazales = self.request.get("edBrazales", "")
            if brazales != "":
                set.brazales = int(brazales)

            faja = self.request.get("edFaja", "")
            if faja != "":
                set.faja = int(faja)

            grebas = self.request.get("edGrebas", "")
            if grebas != "":
                set.grebas = int(grebas)

            set.put()
            time.sleep(1)
            return self.redirect("/panel_sets")
        else:
            return self.redirect("/error?edMsg=" + msg + "&edLink=" + link)


app = webapp2.WSGIApplication([
    ('/sets/guardar_set', GuardarSet)
], debug=True)
