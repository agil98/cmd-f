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
	url = 'https://api.edamam.com/search?q=chicken' + '&app_id=' + app_id + '&app_key=' + app_key + '&from=0&to=4'
	# url = 'https://api.edamam.com/search?q=' + food_name + '&app_id=' + app_id + '&app_key=' + app_key
	r = requests.get(url)
	results = json.loads(r.text)
	recipe_dict = results['hits']

	return '1'

if __name__ == '__main__':
	app.run()
