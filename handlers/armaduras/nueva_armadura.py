# coding=utf-8
# coding = utf-8

import time

import webapp2

from webapp2_extras import jinja2

from model.Habilidad import Habilidad

from model.Armadura import Armadura

from model.Pieza import Pieza

from model.Habilidades_pieza import Habilidades_pieza

from google.appengine.api import users

from functions.Normalize import normalize


class NuevaArmadura(webapp2.RequestHandler):
    def get(self):

        user_name = "Log In"
        user = users.get_current_user()

        if user:
            access_link = users.create_logout_url("/")
            user_name = "Log Out"
        else:
            access_link = users.create_login_url("/")

        habilidades = Habilidad.query().order(Habilidad.nombre)

        template_values = {
            "user_name": user_name,
            "access_link": access_link,
            "habilidades": habilidades
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("nueva_armadura.html", **template_values))

    def post(self):

        nombre = self.request.get("edNombre", "")
        tipos = ["Casco", "Cota", "Brazales", "Faja", "Grebas"]

        msg = "No se ha encontrado un nombre para la armadura"
        link = "/panel_armaduras"

        if nombre.strip() == "":
            return self.redirect("/error?edMsg=" + msg + "&edLink=" + link)

        pk_nombre = normalize(nombre)
        msg = "La armadura ya existe en la Base de Datos"
        if Armadura.query(Armadura.pk_nombre == pk_nombre).count() > 0:
            return self.redirect("/error?edMsg=" + msg + "&edLink=" + link)
        else:
            dictID = {}

            for tipo in tipos:
                nombrePieza = self.request.get("ed" + tipo + "Nombre", "")
                if nombrePieza.strip() != "":
                    pieza = Pieza(nombre=nombrePieza, pieza=tipo)
                    pieza_key = pieza.put()
                    time.sleep(1)
                    dictID[tipo] = pieza_key.id()
                    for n in range(1, 5):
                        habilidadform = self.request.get(tipo + "Habilidad" + str(n), "")
                        if habilidadform.strip() != "":
                            nivel = int(self.request.get(tipo + "Nivel" + str(n), ""))
                            habilidad = Habilidad.get_by_id(int(habilidadform))
                            if nivel > habilidad.nivel_max:
                                nivel = habilidad.nivel_max
                            habilidades_pieza = Habilidades_pieza(pieza=pieza_key.id(), habilidad=habilidad.key.id(),
                                                                  nivel=nivel)
                            habilidades_pieza.put()
                            time.sleep(1)
            armadura = Armadura(nombre=nombre, pk_nombre=pk_nombre)

            armadura.populate(
                casco=dictID.get("Casco"),
                cota=dictID.get("Cota"),
                brazales=dictID.get("Brazales"),
                faja=dictID.get("Faja"),
                grebas=dictID.get("Grebas"))

            armadura.put()
            time.sleep(1)
            return self.redirect("/panel_armaduras")


app = webapp2.WSGIApplication([
    ('/armaduras/nueva_armadura', NuevaArmadura)
], debug=True)
