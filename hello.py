import json
import requests
from flask import Flask, request
from flask_paginate import Pagination, get_page_parameter


app = Flask(__name__)
app_id = '9c6002af'
app_key = '29d5731c89d6adc4fbba5a8e4bbfb1d9'

@app.route('/')
def recipeSearch():
	url = 'https://api.edamam.com/search?q=chicken' + '&app_id=' + app_id + '&app_key=' + app_key
	# url = 'https://api.edamam.com/search?q=' + food_name + '&app_id=' + app_id + '&app_key=' + app_key
	r = requests.get(url)
	# results = json.loads(r.text)
	for x in r.json()['hits']:
		# y = json.dumps((r.json())['hits'][x])
		print(x['recipe'])

	return '1'

	#'https://stackoverflow.com/questions/32911336/what-is-the-difference-between-json-dumps-and-json-load'
	# difference between json.load and json.dump


if __name__ == '__main__':
	app.run()
