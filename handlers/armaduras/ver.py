# coding=utf-8
# coding = utf-8
import time

import webapp2

from google.appengine.ext import ndb
from webapp2_extras import jinja2

from model.Armadura import Armadura
from model.Habilidad import Habilidad
from model.Habilidad_nv import Habilidad_nv

from model.Pieza import Pieza
from model.Habilidades_pieza import Habilidades_pieza

from google.appengine.api import users

from functions import Normalize


class VerArmadura(webapp2.RequestHandler):
    def get(self):

        msg = "Referencia a la armadura perdida"
        link = "/panel_armaduras"

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

        msg = "Armadura no encontrada"

        try:
            clave = ndb.Key(urlsafe=id)
            armadura = clave.get()
        except:
            return self.redirect("/error?edMsg=" + msg + "&edLink=" + link)
        piezas = {}
        hab_total = {}
        habilidades = {}
        tipos = ["Casco", "Cota", "Brazales", "Faja", "Grebas"]

        for tipo in tipos:
            pieza = get_pieza(tipo, armadura)
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


        template_values = {
            "user_name": user_name,
            "access_link": access_link,
            "armadura": armadura,
            "piezas": piezas,
            "habilidades": habilidades,
            "resumen_habilidades": resumen_habilidades
        }

        jinja = jinja2.get_jinja2(app=self.app)

        self.response.write(
            jinja.render_template("ver_armadura.html", **template_values))


app = webapp2.WSGIApplication([
    ('/armaduras/ver', VerArmadura)
], debug=True)


def get_pieza(p_tipo, p_id):
    pieza = None
    if p_id is not None:
        try:
            if p_tipo == "Casco":
                pieza = Pieza.get_by_id(p_id.casco)
            elif p_tipo == "Cota":
                pieza = Pieza.get_by_id(p_id.cota)
            elif p_tipo == "Brazales":
                pieza = Pieza.get_by_id(p_id.brazales)
            elif p_tipo == "Faja":
                pieza = Pieza.get_by_id(p_id.faja)
            elif p_tipo == "Grebas":
                pieza = Pieza.get_by_id(p_id.grebas)
        except:
            pieza = None
    return pieza
