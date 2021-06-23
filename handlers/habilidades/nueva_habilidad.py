# coding = utf-8

import webapp2

from webapp2_extras import jinja2


from google.appengine.api import users


class NuevaHabilidad(webapp2.RequestHandler):
    def get(self):

        user_name = "Log In"
        user = users.get_current_user()

        if user:
            access_link = users.create_logout_url("/")
            user_name = "Log Out"
        else:
            access_link = users.create_login_url("/")

        template_values = {
            "user_name": user_name,
            "access_link": access_link,
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("nueva_habilidad.html", **template_values))

    def post(self):

        str_nvmax = self.request.get("edNvmax", "")


        try:
            nvmax = int(str_nvmax)
        except ValueError:
            nvmax = -1

        if (nvmax < 0):
            return self.redirect("/habilidades/nueva_habilidad")
        else:
            return self.redirect("/habilidades/nueva_habilidad_2?&nvmax=" + str_nvmax)

app = webapp2.WSGIApplication([
    ('/habilidades/nueva_habilidad', NuevaHabilidad)
], debug=True)
