import webapp2
from webapp2_extras import jinja2
# coding = utf-8
from google.appengine.api import users

class PanelAdmin(webapp2.RequestHandler):
    def get(self):

        user_name = "Log In"
        user = users.get_current_user()
        nickname = user.nickname()

        if user:
            access_link = users.create_logout_url("/")
            user_name = "Log Out"
        else:
            access_link = users.create_login_url("/")

        template_values = {
            "user_name": user_name,
            "access_link": access_link,
            "nickname": nickname
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("administracion.html", **template_values))


app = webapp2.WSGIApplication([
    ('/panel_admin', PanelAdmin)
], debug=True)
