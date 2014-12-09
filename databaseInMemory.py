# this is a simple implementation of a data store i can use when 
# testing this code on my ipad

data = {}

def get(id):
	if id in data:
		return data[id]
	else:
		return None
		
def put(id, value):
	data[id] = value
