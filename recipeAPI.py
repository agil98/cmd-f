import requests
import json
from flask import render_template


app_id = '9c6002af'
app_key = '048cc175d1a6141040a85f9fb7c55cf5'


# @app.route('/choose-recipe/<label>')
# def recipe_search(label, img_addr):
def recipe_search(label):
    label.replace(" ", "+")
    url = 'https://api.edamam.com/search?q=' + label + '&app_id=' + app_id + '&app_key=' + app_key + '&from=0&to=4'
    response = requests.get(url)
    results = json.loads(response.text)
    recipes = results["hits"]
    print(recipes)

    # return render_template("recipe.html", img_addr=img_addr, recipes=recipes)
    return render_template("recipe.html", recipes=recipes)
