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
import caesar
import cgi


def build_page(textarea_content):
    header_message = "Web Caesar"
    header = "<h1>" + header_message + "</h1>"

    rotation_label = "<label>Rotate by:</label>"
    rotation_input = "<input type='number' name='rotation'/>"

    message_label = "<label>Type a message:</label>"
    submit = '<br>' + '<input type="submit">' + '</input>'
    text_area = '<textarea name="message">' + textarea_content + '</textarea>'

    form = '<form method="post">' + rotation_label + rotation_input + '<br>' + message_label + text_area + '<br>' + submit + '</form>'

    content = header + form
    return content


def error_page():
    header_message = "Error! Your input was invalid. Please try again."
    header = "<h1>" + header_message + "</h1>"
    return header


class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page("")
        self.response.write(content)

    def post(self):
        keyvalue = self.request.get("message")
        rotation_value = self.request.get('rotation')

        if not isinstance(rotation_value, int):
            content = error_page()
            return self.response.write(content)
        else:
            rotation = int(self.request.get('rotation'))
            encrypted_message = caesar.encrypt(keyvalue, rotation)
            escaped_message = cgi.escape(encrypted_message)
            content = build_page(escaped_message)
            return self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
