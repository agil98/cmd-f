import json
import requests
import logging
import os
import base64
import googleVisionAPI
from flask import Flask, request, render_template, send_from_directory, jsonify
from werkzeug.utils import secure_filename

STATIC_DIR = 'static/uploaded_images'
app = Flask(__name__)
app.config['STATIC_DIR'] = STATIC_DIR


@app.route('/')
def hello():
	return render_template('hello.html')


@app.route('/search-label', methods=['POST'])
def info_back():
	# # given local image
	img = request.files['img-upload']
	if img.filename != '':
		img_name = secure_filename(img.filename)
		path_addr = os.path.join(app.config['STATIC_DIR'], img_name)
		img.save(path_addr)
		app.logger.info('%s image path address saved' % path_addr)
		img_info = {"uri": path_addr, "label": get_label(path_addr)}
		return json.dumps(img_info)
	else:
		# # given link address
		app.logger.info('%s image link address saved' % request.form['img_url'])
		img_url = request.form['img_url']
		return img_url, get_label(img_url)


def get_label(img_path):
	label = googleVisionAPI.search_labels(image_address=img_path)
	# print(label)
	return label


# https://cloud.google.com/vision/docs/base64#mac-osx
# https://www.techcoil.com/blog/how-to-use-python-3-to-convert-your-images-to-base64-encoding/
def encode_image(image_path):
	with open(image_path, "rb") as img_file:
		image_content = img_file.read()
		return base64.b64encode(image_content).decode('utf-8')


if __name__ == '__main__':
	app.run(debug=True)
