import json
import requests
from flask import render_template, request
from flask_paginate import Pagination, get_page_parameter


app_id = '9c6002af'
app_key = '048cc175d1a6141040a85f9fb7c55cf5'


# @app.route('/choose-recipe/<label>')
def recipe_search(label):
    print('the label in the recipeAPI function is : ' + label)
    url = 'https://api.edamam.com/search?q=Frozen+Dessert' + '&app_id=' + app_id + '&app_key=' + app_key + '&from=0&to=4'
    # url = 'https://api.edamam.com/search?q=' + label + '&app_id=' + app_id + '&app_key=' + app_key + '&from=0&to=4'
    r = requests.get(url)
    results = json.loads(r.text) # this gives a dictionary object
    print(results)
    recipe_dict = results['hits']

    return render_template("recipe.html", recipes=recipe_dict)
