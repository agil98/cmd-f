import json
import requests
from flask import Flask


app = Flask(__name__)
API_KEY = 'b36d687785msh07f8dded993900fp124f55jsn1302007a713a'

@app.route('/')
def hello():
	url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/quickAnswer?q=How+much+vitamin+c+is+in+2+apples%3F'
	headers = {'X-RapidAPI-Key': API_KEY}
	r = requests.get(url, headers=headers)
	return json.dumps(r.json())



if __name__ == '__main__':
	app.run()
