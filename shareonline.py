from bottle import get, route, run, request, response, HTTPError
import random
import databaseInMemory as database

random.seed()

def random_id():
	id = ''
	for i in range(1,10):
		id += str(random.randint(0,9))
	return id

def create_document(content):
	new_doc = random_id()
	database.put(new_doc, content)
	return new_doc
	
@route('/share')
def share():
	content = request.params.content
	ret = { 'id': create_document(content) }
	return ret
	
@get('/share/<id>')
def access(id):
	content = database.get(id)
	if content:
		response.content_type = 'text/plain'
		return content
	else:
		return HTTPError(404)

run(host='localhost', port=8080, debug=True)
