# coding=utf-8
# coding = utf-8
import time

import webapp2

from google.appengine.ext import ndb

from webapp2_extras import jinja2

from model.Habilidad import Habilidad

from model.Habilidad_nv import Habilidad_nv

from google.appengine.api import users


class EditarHabilidad(webapp2.RequestHandler):

    def get(self):

        msg = "Referencia a la habilidad perdida"
        link = "/panel_habilidades"

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

        msg = "Habilidad no encontrada"
        try:
            clave = ndb.Key(urlsafe=id)
            habilidad = clave.get()

            habilidad_nv = Habilidad_nv.query(ancestor=clave).order(Habilidad_nv.nivel)

        except:
            return self.redirect("/error?edMsg=" + msg + "&edLink=" + link)

        template_values = {
            "user_name": user_name,
            "access_link": access_link,
            "habilidad": habilidad,
            "habilidad_nv": habilidad_nv,
            "id": id
        }

        jinja = jinja2.get_jinja2(app=self.app)

        self.response.write(
            jinja.render_template("editar_habilidad.html", **template_values))

    def post(self):

        msg = "Referencia a la habilidad perdida"
        link = "/panel_habilidades"

        try:
            id = self.request.get('edId')
        except:
            return self.redirect("/error?edMsg=" + msg + "&edLink=" + link)

        desgen = self.request.get("edDescrip", "")

        msg = "Habilidad no encontrada"
        try:
            clave = ndb.Key(urlsafe=id)
            habilidad = clave.get()

            habilidad_query = Habilidad_nv.query(ancestor=clave).order(Habilidad_nv.nivel)

        except:
            return self.redirect("/error?edMsg=" + msg + "&edLink=" + link)

        habilidad.descripcion = desgen
        habilidad.put()
        time.sleep(1)

        x = 1
        for habilidad_nv in habilidad_query:
            descrip = self.request.get("edDescrip" + str(x), "")
            habilidad_nv.descripcion = descrip
            habilidad_nv.put()
            x += 1;

        time.sleep(1)
        return self.redirect('/habilidades/ver?id=' + id)


app = webapp2.WSGIApplication([
    ('/habilidades/editar', EditarHabilidad)
], debug=True)
