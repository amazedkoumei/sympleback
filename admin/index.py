# -*- coding: utf-8 -*-
#
# admin/index for sypleback v0.1
#
# Copyright (c) 2012 amazedkoumei (Twitter: @amazedkoumei, Blog:http://blog.amazedkoumei.com)
# Licensed under the MIT license + "keep this comment block even if you modify it".
#
# History:
#  07-20-2012 new created
#
import os, logging, datetime
from api.feedback import Feedback
from google.appengine.ext import webapp, db
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

class MyPage(webapp.RequestHandler):
	def get(self):
		
		query = Feedback.all()
		query.filter("is_done = ", False)
		query.filter("is_starred = ", False)
		query.order('-insert_datetime')
		feedbackDict = {}
		insert_date = "";
		for feedback in query:
			if insert_date != feedback.insert_datetime.strftime("%a %b %d %Y"):
				insert_date = feedback.insert_datetime.strftime("%a %b %d %Y")
				feedbackDict[insert_date] = []
			feedback.insert_date = feedback.insert_datetime.strftime("%a %b %d %Y")
			feedback.insert_time = feedback.insert_datetime.strftime("%H:%M:%S")
			feedbackDict[insert_date].append(feedback)
		
		template_values = {
			"feedbackDict" : feedbackDict
		}
		path = os.path.join(os.path.dirname(__file__), 'index.html')
		logging.debug(path)
		self.response.out.write(template.render(path, template_values))
		
application = webapp.WSGIApplication([('/admin', MyPage)
																		], debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()
