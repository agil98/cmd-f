import json
import os
import googleVisionAPI
import recipeAPI
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

STATIC_DIR = 'static/uploaded_images'
app = Flask(__name__)
app.config['STATIC_DIR'] = STATIC_DIR
# app.add_url_rule('/choose-recipe/?=<img_addr>', view_func=recipeAPI.recipe_search)
app.add_url_rule('/choose-recipe/<label>', view_func=recipeAPI.recipe_search)


@app.route('/')
def hello():
	return render_template('index.html')


@app.route('/search-label', methods=['POST'])
def info_back():
	# # given local image
	img = request.files['local-img-file']
	if img.filename != '':
		img_name = secure_filename(img.filename)
		path_addr = os.path.join(app.config['STATIC_DIR'], img_name)
		img.save(path_addr)
		app.logger.info('%s image path address saved' % path_addr)
		img_info = {"uri": path_addr, "label": get_label('local', path_addr)}
		return json.dumps(img_info)
	else:
		# # given link address
		app.logger.info('%s image link address saved' % request.form['img_url'])
		img_url = request.form['img_url']

		return json.dumps({"uri": img_url, "label": get_label('online', img_url)})


def get_label(location, img_path):
	return googleVisionAPI.search_labels(location=location, image_address=img_path)


if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)
