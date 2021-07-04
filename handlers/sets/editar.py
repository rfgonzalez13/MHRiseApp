# coding=utf-8
# coding = utf-8
import time

import webapp2

from google.appengine.ext import ndb

from webapp2_extras import jinja2

from model.Set import Set

from model.Pieza import Pieza

from google.appengine.api import users


class EditarSet(webapp2.RequestHandler):

    def get(self):

        msg = "Referencia al set perdido"
        link = "/panel_sets"

        try:
            id = self.request.get('id')
        except:
            return self.redirect("/error?edMsg=" + msg + "&edLink=" + link)

        user_name = "Log In"
        user = users.get_current_user()

        if user:
            access_link = users.create_logout_url("/")
            user_name = "Log Out"
        else:
            access_link = users.create_login_url("/")

        msg = "Set no encontrado"
        try:
            clave = ndb.Key(urlsafe=id)
            set = clave.get()
        except:
            return self.redirect("/error?edMsg=" + msg + "&edLink=" + link)

        cascos = Pieza.query(Pieza.pieza == "Casco").order(Pieza.nombre)
        cotas = Pieza.query(Pieza.pieza == "Cota").order(Pieza.nombre)
        brazales = Pieza.query(Pieza.pieza == "Brazales").order(Pieza.nombre)
        fajas = Pieza.query(Pieza.pieza == "Faja").order(Pieza.nombre)
        grebas = Pieza.query(Pieza.pieza == "Grebas").order(Pieza.nombre)

        nombres = {}

        if set.casco is not None:
            pieza = Pieza.get_by_id(set.casco)
            nombres["Casco"] = pieza.nombre
        if set.cota is not None:
            pieza = Pieza.get_by_id(set.cota)
            nombres["Cota"] = pieza.nombre
        if set.brazales is not None:
            pieza = Pieza.get_by_id(set.brazales)
            nombres["Brazales"] = pieza.nombre
        if set.faja is not None:
            pieza = Pieza.get_by_id(set.faja)
            nombres["Faja"] = pieza.nombre
        if set.grebas is not None:
            pieza = Pieza.get_by_id(set.grebas)
            nombres["Grebas"] = pieza.nombre

        template_values = {
            "user_name": user_name,
            "access_link": access_link,
            "set": set,
            "id": id,
            "cascos": cascos,
            "cotas": cotas,
            "brazales": brazales,
            "fajas": fajas,
            "grebas": grebas,
            "nombres": nombres
        }

        jinja = jinja2.get_jinja2(app=self.app)

        self.response.write(
            jinja.render_template("editar_set.html", **template_values))

    def post(self):

        msg = "Referencia al set perdido"
        link = "/panel_sets"

        try:
            id = self.request.get('edId')
        except:
            return self.redirect("/error?edMsg=" + msg + "&edLink=" + link)

        casco = self.request.get("edCasco", "")
        cota = self.request.get("edCota", "")
        brazales = self.request.get("edBrazales", "")
        faja = self.request.get("edFaja", "")
        grebas = self.request.get("edGrebas", "")

        msg = "Set no encontrado"
        try:
            clave = ndb.Key(urlsafe=id)
            set = clave.get()
        except:
            return self.redirect("/error?edMsg=" + msg + "&edLink=" + link)

        if casco != "":
            set.casco = int(casco)
        else:
            set.casco = None

        if cota != "":
            set.cota = int(cota)
        else:
            set.cota = None

        if brazales != "":
            set.brazales = int(brazales)
        else:
            set.brazales = None

        if faja != "":
            set.faja = int(faja)
        else:
            set.faja = None

        if grebas != "":
            set.grebas = int(grebas)
        else:
            set.grebas = None

        set.put()
        time.sleep(1)

        return self.redirect('/sets/ver?id=' + id)


app = webapp2.WSGIApplication([
    ('/sets/editar', EditarSet)
], debug=True)
