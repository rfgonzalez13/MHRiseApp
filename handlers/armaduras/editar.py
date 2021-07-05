# coding=utf-8
# coding = utf-8


import webapp2


class EditarArmadura(webapp2.RequestHandler):

    def get(self):
        msg = "Editar no implementado en esta version"
        link = "/panel_armaduras"

        return self.redirect("/error?edMsg=" + msg + "&edLink=" + link)


app = webapp2.WSGIApplication([
    ('/armaduras/editar', EditarArmadura)
], debug=True)
