import webapp2
import caesar


class Index(webapp2.RequestHandler):
    def get(self):
        message = "Hellooooo world!"
        encrypted_message = caesar.encrypt(message, 13)



        self.response.write(encrypted_message)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
