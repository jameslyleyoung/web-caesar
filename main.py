import webapp2
import caesar


class Index(webapp2.RequestHandler):
    def get(self):
        message = "Hellooooo world!"
        encrypted_message = caesar.encrypt(message, 13)

        textarea = "<textarea>" + encrypted_message + "</textarea>"
        submit = "<input type='submit'/>"
        form = "<form action=''>" + textarea + "<br>" + submit + "</form>"

        self.response.write(form)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
