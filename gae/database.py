from google.appengine.ext import ndb

class StoredValue(ndb.Model):
  value = ndb.StringProperty()

def put(id, value):
	StoredValue(id=id, value=value).put()

def get(id):
	res = StoredValue.get_by_id(id)
	if res: return res.value
	else: return None

def all():
	return [id.id() for id in StoredValue.query().iter(keys_only=True)]
