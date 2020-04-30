import json
import requests
from flask import Flask, request, render_template
from flask_paginate import Pagination, get_page_parameter


app = Flask(__name__)
app_id = '9c6002af'
app_key = '048cc175d1a6141040a85f9fb7c55cf5'
ingredients = {}
# name = {}
# url = {}
# servings = {}
# image = {}

@app.route('/')
def recipeSearch():
	url = 'https://api.edamam.com/search?q=chicken' + '&app_id=' + app_id + '&app_key=' + app_key + '&from=0&to=4'
	res = requests.get(url)
	results = res.json()

	return render_template("recipe.html", recipes=results['hits'])

if __name__ == '__main__':
	app.run()
