import json
import requests
from flask import Flask, request


app = Flask(__name__)
app_id = '9c6002af'
app_key = '29d5731c89d6adc4fbba5a8e4bbfb1d9'

@app.route('/')
def hello():
	url = 'https://api.edamam.com/search?q=' + food_name + '&app_id=' + app_id + '&app_key=' + app_key
	#'https://api.edamam.com/search?q=chicken&app_id=9c6002af&app_key=29d5731c89d6adc4fbba5a8e4bbfb1d9&from=0&to=3&calories=591-722&health=alcohol-free'
	#url = 'https://api.edamam.com/search?q=' + food_name + '&app_id=' + app_id + '&app_key=' + app_key
	r = requests.get(url)
	return json.dumps(r.json())



if __name__ == '__main__':
	app.run()
