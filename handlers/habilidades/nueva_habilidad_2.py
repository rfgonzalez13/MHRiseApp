# coding = utf-8

import time

import webapp2

from webapp2_extras import jinja2

from model.Habilidad import Habilidad

from model.Habilidad_nv import Habilidad_nv

from google.appengine.api import users

from functions.Normalize import normalize


class NuevaHabilidad2(webapp2.RequestHandler):
    def get(self):

        nvmax = self.request.get('nvmax')
        user_name = "Log In"
        user = users.get_current_user()

        if user:
            access_link = users.create_logout_url("/")
            user_name = "Log Out"
        else:
            access_link = users.create_login_url("/")

        try:
            i_nvmax = int(nvmax)
        except ValueError:
            i_nvmax = -1

        template_values = {
            "user_name": user_name,
            "access_link": access_link,
            "nvmax": i_nvmax
        }

        jinja = jinja2.get_jinja2(app=self.app)
        if 0 < i_nvmax < 8:
            self.response.write(
                jinja.render_template("nueva_habilidad_2.html", **template_values))
        else:
            self.response.write(
                jinja.render_template("nueva_habilidad.html", **template_values))

    def post(self):

        str_nvmax = self.request.get("edNvmax", "")
        nombre = self.request.get("edNombre", "")
        desgen = self.request.get("edDescrip", "")
        nvmax = int(str_nvmax)

        pk_nombre = normalize(nombre)

        msg = "La habilidad ya existe en la Base de Datos"
        link = "/panel_habilidades"

        if Habilidad.query(Habilidad.pk_nombre == pk_nombre).count() > 0:
            return self.redirect("/error?edMsg=" + msg + "&edLink=" + link)
        else:
            habilidad = Habilidad(nombre=nombre, nivel_max=nvmax, descripcion=desgen, pk_nombre=pk_nombre)
            key = habilidad.put()
            time.sleep(1)

            for nv in range(1, nvmax + 1):
                descrip = self.request.get("edDescrip" + str(nv), "")
                habilidad_nv = Habilidad_nv(habilidad=key, nivel=nv, descripcion=descrip, parent=key)
                habilidad_nv.put()
                time.sleep(1)

            return self.redirect("/panel_habilidades")


app = webapp2.WSGIApplication([
    ('/habilidades/nueva_habilidad_2', NuevaHabilidad2)
], debug=True)
