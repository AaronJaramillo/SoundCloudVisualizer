from __future__ import unicode_literals

from django.apps import AppConfig

import web
import SCVis


class SvappConfig(AppConfig):
    name = 'svapp'

    def POST(self):
		print("WAAAAAAAASUP")
		
		form = web.input(name="Nobody", greet="Hello")
		greeting = "%s, %s" % (form.greet, form.name)
		return render.index(greeting = greeting)

urls = (
  '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
	name = 'render'
    def GET(self):
        return render.hello_form()

if __name__ == "__main__":
    app.run()