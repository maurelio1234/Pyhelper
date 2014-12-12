
running_in_ipad = False

try:
	from google.appengine.ext.webapp.util import run_wsgi_app
	from gae import bottle
	import databaseInMemory as database
except ImportError: # i.e. if running in my iPad
	import bottle
	import databaseInMemory as database
	running_in_ipad = True 
	
import random
from bottle import get, route, run, request, response, HTTPError, Bottle

random.seed()

bottle = Bottle()

def random_id():
	id = ''
	for i in range(1,10):
		id += str(random.randint(0,9))
	return id

def create_document(content):
	new_doc = random_id()
	database.put(new_doc, content)
	return new_doc
	
@bottle.route('/share')
def share():
	content = request.params.content
	ret = { 'id': create_document(content) }
	return ret
	
@bottle.get('/share/<id>')
def access(id):
	content = database.get(id)
	if content:
		response.content_type = 'text/plain'
		return content
	else:
		return HTTPError(404)

if running_in_ipad:
	run(host='localhost', port=8080, debug=True, app=bottle)
