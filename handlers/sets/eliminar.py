# coding=utf-8
# coding = utf-8
import time

import webapp2

from google.appengine.ext import ndb

from webapp2_extras import jinja2

from model.Set import Set


class EliminarSet(webapp2.RequestHandler):

    def get(self):

        msg = "Referencia al set perdida"
        link = "/panel_sets"

        try:
            id = self.request.get('id')
        except:
            return self.redirect("/error?edMsg=" + msg + "&edLink=" + link)

        msg = "Set no encontrado"
        try:
            clave_set = ndb.Key(urlsafe=id)
        except:
            return self.redirect("/error?edMsg=" + msg + "&edLink=" + link)

        clave_set.delete()

        time.sleep(1)
        return self.redirect("/panel_sets")


app = webapp2.WSGIApplication([
    ('/sets/eliminar', EliminarSet)
], debug=True)
