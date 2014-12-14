
generated_id_length = 10
force_ipad_mode_on_gae = False 

try:
	if force_ipad_mode_on_gae: 
		raise ImportError()

	from google.appengine.ext.webapp.util import run_wsgi_app
	from gae import database
	from gae.bottle import Bottle, HTTPError, request, response
	running_in_ipad = False
except ImportError: 
	from test import database
	if force_ipad_mode_on_gae:
		from gae.bottle import Bottle, HTTPError, request, response
	else:
		from bottle import run, Bottle, HTTPError, request, response
	running_in_ipad = True 
	
import random

random.seed()

if running_in_ipad and not force_ipad_mode_on_gae:
	bottle = Bottle()
else:
	# adding catchall so that I will get exception stack traces when debugging
	bottle = Bottle(catchall=False) 

def random_id():
	id = ''
	for i in range(1,generated_id_length):
		id += str(random.randint(0,9))
	return id

def create_document(content):
	new_doc = random_id()
	database.put(new_doc, content)
	return new_doc
	
@bottle.route('/share', method=['GET', 'POST'])
def share():
	content = request.params.content
	if content: # TODO: in the future, support proper RESTfulness
		ret = { 'id': create_document(content) }
		return ret
	else:
		ret = ""
		for item in database.all():
			ret += str(item) + "\n"
		return ret
	
@bottle.get('/share/<id>')
def access(id):
	content = database.get(id)
	if content:
		response.content_type = 'text/html'

		from plaintext2html import plaintext2html
		return "<html><head><title>"+str(id)+"</title></head><body>"+plaintext2html(content)+"</body></html>"
	else:
		return HTTPError(404)

if running_in_ipad and not force_ipad_mode_on_gae:
	run(host='localhost', port=8080, debug=True, app=bottle)
