import webapp2

class Index(webapp2.RequestHandler):
    def get(self):
        self.response.write("helllllllllo")

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
