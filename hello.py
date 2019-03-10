import json
import requests
import logging
import os
from flask import Flask, request, render_template, send_from_directory, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def hello():
   return render_template('hello.html')

@app.route('/food',methods=['POST'])
def infoback():
	if 'file' in request.files:
		filepath = os.path.join(app.instance_path)
		f = request.files['file']
		filename = secure_filename(f.filename)
		f.save(filepath, filename)
		app.logger.info('%s saved' % filename)
	return render_template('hello.html', filename='%s/%s' % (filepath, filename))
	# return jsonify(image1="http://www.caribfocus.com/wp-content/uploads/2015/09/apples2.jpg",description="This is an apple")

if __name__ == '__main__':
   app.run(debug = True)	
