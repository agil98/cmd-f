import json
import requests
from flask import Flask, request
from flask_paginate import Pagination, get_page_parameter


app = Flask(__name__)
app_id = '9c6002af'
app_key = '29d5731c89d6adc4fbba5a8e4bbfb1d9'
ingredients = {}
# name = {}
# url = {}
# servings = {}
# image = {}


@app.route('/')
def recipeSearch():
	url = 'https://api.edamam.com/search?q=chicken' + '&app_id=' + app_id + '&app_key=' + app_key + '&from=0&to=9'
	# url = 'https://api.edamam.com/search?q=' + food_name + '&app_id=' + app_id + '&app_key=' + app_key
	r = requests.get(url)
	results = json.loads(r.text)
	# return json.dumps(r.json()['hits'])

	for x in r.json()['hits']: # seperate the recipes into different arrays
		# y = json.dumps((r.json())[x])
		# json.dumps(x['recipe']['ingredientLines'])
		# print(x['recipe']['image'])
		for key,value in x.items():
			ingredients[key] = value # making the dict x as the index of dict ingredients. Hence, the unhashable error
			print key
		# name[x] = x['recipe']['labels']
		# url[x] = x['recipe']['url']
		# servings[x] = x['recipe']['yield']
		# image[x] = x['recipe']['image']

	return '1'

	#'https://stackoverflow.com/questions/32911336/what-is-the-difference-between-json-dumps-and-json-load'
	# difference between json.load and json.dump


if __name__ == '__main__':
	app.run()
