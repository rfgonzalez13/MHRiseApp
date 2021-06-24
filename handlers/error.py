# coding=utf-8
# coding = utf-8

import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users


class Error(webapp2.RequestHandler):
    def get(self):

        try:
            link = self.request.get("edLink")
        except:
            link = "/"

        try:
            msg = self.request.get('edMsg')
        except:
            msg = None
            link = "/"

        if not msg:
            msg = "Error Fatal, ne sabemos qué ha pasado :("

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
            "nickname": nickname,
            "msg": msg,
            "link": link
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("error.html", **template_values))


app = webapp2.WSGIApplication([
    ('/error', Error)
], debug=True)
