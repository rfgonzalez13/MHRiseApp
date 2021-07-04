# coding=utf-8
# coding = utf-8

import time

import webapp2

from webapp2_extras import jinja2

from model.Set import Set
from model.Habilidad import Habilidad
from model.Habilidad_nv import Habilidad_nv

from model.Pieza import Pieza
from model.Habilidades_pieza import Habilidades_pieza

from google.appengine.api import users

from functions import Normalize


class NuevoSet(webapp2.RequestHandler):
    def get(self):

        user_name = "Log In"
        user = users.get_current_user()

        if user:
            access_link = users.create_logout_url("/")
            user_name = "Log Out"
        else:
            access_link = users.create_login_url("/")

        cascos = Pieza.query(Pieza.pieza == "Casco").order(Pieza.nombre)
        cotas = Pieza.query(Pieza.pieza == "Cota").order(Pieza.nombre)
        brazales = Pieza.query(Pieza.pieza == "Brazales").order(Pieza.nombre)
        fajas = Pieza.query(Pieza.pieza == "Faja").order(Pieza.nombre)
        grebas = Pieza.query(Pieza.pieza == "Grebas").order(Pieza.nombre)

        template_values = {
            "user_name": user_name,
            "access_link": access_link,
            "cascos": cascos,
            "cotas": cotas,
            "brazales": brazales,
            "fajas": fajas,
            "grebas": grebas
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("nuevo_set.html", **template_values))

    def post(self):

        nombre = self.request.get("edNombre", "")

        user_name = "Log In"
        user = users.get_current_user()

        if user:
            access_link = users.create_logout_url("/")
            user_name = "Log Out"
        else:
            access_link = users.create_login_url("/")

        msg = "No se ha encontrado un nombre para el set"
        link = "/sets/nuevo_set"

        if nombre.strip() == "":
            return self.redirect("/error?edMsg=" + msg + "&edLink=" + link)

        piezas = {}
        hab_total = {}
        habilidades = {}
        tipos = ["Casco", "Cota", "Brazales", "Faja", "Grebas"]
        ids = {}
        for tipo in tipos:
            idPieza = self.request.get("ed" + tipo, "")
            ids[tipo] = idPieza
            if idPieza != "":
                pieza = Pieza.get_by_id(int(idPieza))
            else:
                pieza = None
            lista_h = []
            if pieza is not None:
                piezas[tipo] = pieza.nombre
                habilidades_pieza = Habilidades_pieza.query(Habilidades_pieza.pieza == int(pieza.key.id()))
                for h in habilidades_pieza:
                    habilidad = Habilidad.get_by_id(h.habilidad)
                    if hab_total.get(habilidad.nombre) is not None:
                        new_nivel = hab_total.get(habilidad.nombre) + h.nivel
                    else:
                        new_nivel = h.nivel
                    hab_total.update({habilidad.nombre: new_nivel})
                    lista_h.append(habilidad.nombre + u" Nv" + str(h.nivel))
                habilidades[pieza.nombre] = lista_h
        resumen_habilidades = {}
        for h in hab_total:
            datos_habilidad = {}
            pk_nombre = Normalize.normalize(h)
            habilidad = Habilidad.query(Habilidad.pk_nombre == pk_nombre).get()
            nivel = hab_total.get(habilidad.nombre)
            if nivel > habilidad.nivel_max:
                nivel = habilidad.nivel_max
            habilidad_nv = Habilidad_nv.query(Habilidad_nv.nivel == nivel, ancestor=habilidad.key).get()
            datos_habilidad["nv"] = nivel
            datos_habilidad["descrip_nv"] = habilidad_nv.descripcion
            datos_habilidad["descrip"] = habilidad.descripcion
            datos_habilidad["nv_max"] = habilidad.nivel_max - nivel
            resumen_habilidades[habilidad.nombre] = datos_habilidad

        armadura = {"nombre": nombre}
        links = {"volver": "/sets/nuevo_set", "entidad": "sets"}
        template_values = {
            "user_name": user_name,
            "access_link": access_link,
            "piezas": piezas,
            "armadura": armadura,
            "habilidades": habilidades,
            "resumen_habilidades": resumen_habilidades,
            "links": links,
            "ids": ids
        }

        jinja = jinja2.get_jinja2(app=self.app)

        self.response.write(
            jinja.render_template("ver_armadura.html", **template_values))


app = webapp2.WSGIApplication([
    ('/sets/nuevo_set', NuevoSet)
], debug=True)
