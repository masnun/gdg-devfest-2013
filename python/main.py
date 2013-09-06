import webapp2

class Main(webapp2.RequestHandler):
  def get(self):
    self.response.out.write('Hello, DevFest 2013!')

    
app = webapp2.WSGIApplication([
  ('/', Main),
], debug=True)
