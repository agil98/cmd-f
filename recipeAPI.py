import requests
import json
from flask import render_template, request


app_id = '9c6002af'
app_key = '048cc175d1a6141040a85f9fb7c55cf5'


def recipe_search():
    data = json.loads(request.data)
    label = data["label"]
    img_addr = data["uri"]

    label.replace(" ", "+")
    url = 'https://api.edamam.com/search?q=' + label + '&app_id=' + app_id + '&app_key=' + app_key
    response = requests.get(url)
    results = json.loads(response.text)
    recipes = results["hits"]

    return json.dumps(render_template("recipe.html", img_addr=img_addr, recipes=recipes))
