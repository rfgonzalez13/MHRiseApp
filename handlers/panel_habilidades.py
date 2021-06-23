# coding = utf-8
import webapp2
from webapp2_extras import jinja2

from google.appengine.api import users

from model.Habilidad import Habilidad

class PanelHabilidad(webapp2.RequestHandler):
    def get(self):

        user_name = "Log In"
        user = users.get_current_user()

        if user:
            access_link = users.create_logout_url("/")
            user_name = "Log Out"
        else:
            access_link = users.create_login_url("/")

        habilidades = Habilidad.query().order(Habilidad.nombre, Habilidad.nivel)

        template_values = {
            "user_name": user_name,
            "access_link": access_link,
            "habilidades": habilidades
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("habilidades_showall.html", **template_values))


app = webapp2.WSGIApplication([
    ('/panel_habilidades', PanelHabilidad)
], debug=True)
