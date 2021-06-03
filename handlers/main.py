# coding = utf-8
#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


import webapp2
from webapp2_extras import jinja2

from google.appengine.api import users

class MainHandler(webapp2.RequestHandler):
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
            "access_link": access_link
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("index.html", **template_values))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
