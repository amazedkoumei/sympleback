# -*- coding: utf-8 -*-
#
# api-Feedback for sypleback v0.1
#
# Copyright (c) 2012 amazedkoumei (Twitter: @amazedkoumei, Blog:http://blog.amazedkoumei.com)
# Licensed under the MIT license + "keep this comment block even if you modify it".
#
# History:
#  07-20-2012 new created
#
from google.appengine.ext import webapp, db
from google.appengine.ext.webapp.util import run_wsgi_app

class Feedback(db.Model):
	service_name = db.StringProperty(required=True)
	twitter = db.StringProperty()
	email = db.StringProperty()
	message = db.TextProperty(required=True)
	is_done = db.BooleanProperty(default=False)
	is_starred = db.BooleanProperty(default=False)
	tag_list = db.StringListProperty()
	insert_datetime = db.DateTimeProperty(auto_now_add=True)
	update_datetime = db.DateTimeProperty(auto_now=True)



class FeedbackPost(webapp.RequestHandler):
	def post(self):
		try:
			service_name = self.request.get("service_name")
			twitter = self.request.get("twitter")
			email = self.request.get("email")
			message = self.request.get("message")
			
			feedback = Feedback(
								service_name = service_name
								,twitter = twitter
								,email = email
								,message = message
			)
			
			feedback.put()
			
			result = "OK"
			self.response.set_status(200)
			self.response.out.write(result)
			
		except db.Error, e:
			result = e
			self.response.set_status(500)
			self.response.out.write(e)
		except:
			self.response.set_status(500)
			self.response.out.write("NG")
			
application = webapp.WSGIApplication([('/api/feedback/post', FeedbackPost)
																		], debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()
