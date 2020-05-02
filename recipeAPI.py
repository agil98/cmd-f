import json
import requests
from flask import Flask, request, render_template
from flask_paginate import Pagination, get_page_parameter


app = Flask(__name__)
app_id = '9c6002af'
app_key = '048cc175d1a6141040a85f9fb7c55cf5'
ingredients = {}
food_name = {}
# url = {}
# servings = {}
# image = {}


@app.route('/food')
def recipeSearch():
    # url = 'https://api.edamam.com/search?q=chicken' + '&app_id=' + app_id + '&app_key=' + app_key + '&from=0&to=4'
    url = 'https://api.edamam.com/search?q=' + food_name + '&app_id=' + app_id + '&app_key=' + app_key + '&from=0&to=4'
    r = requests.get(url)
    results = json.loads(r.text) # this gives a dictionary object
    recipe_dict = results['hits']

    return render_template("recipe.html", recipes=recipe_dict)


if __name__ == '__main__':
    app.run()
