import json
import requests
import logging
import os
from flask import Flask, request, render_template, send_from_directory, jsonify
from werkzeug.utils import secure_filename

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(APP_ROOT, 'static')
app = Flask(__name__)


@app.route('/')
def hello():
   return render_template('hello.html')


@app.route('/food', methods=['POST'])
def infoBack():
	app.logger.info(request.form['img_url'])
	img_url = request.form['img_url']

	# if 'file' in request.files:
	# 	f = request.files['file']
	# 	filename = secure_filename(f.filename)
	# 	f.save(STATIC_DIR, filename)
	# 	app.logger.info('%s saved' % filename)
	# return render_template('hello.html', filename='%s/%s' % (STATIC_DIR, filename))
	# return jsonify(image1="http://www.caribfocus.com/wp-content/uploads/2015/09/apples2.jpg",description="This is an apple")
	return str(img_url)

# @app.route('/food',methods=['POST'])
# def infopresent():
# 	return render_template('seeyou.html')


if __name__ == '__main__':
	app.run(debug=True)
