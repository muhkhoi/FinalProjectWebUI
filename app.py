import os

#from flaskext.uploads import UploadSet, configure_uploads, IMAGES
from flask import Flask, request, render_template, send_from_directory
from flask_uploads import UploadSet, configure_uploads, IMAGES

__author__ = 'ibininja'

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/cc'
configure_uploads(app, photos)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
	image_names = os.listdir('static/images')
	return render_template("index.html", image_names=image_names)

@app.route("/stream")
def realtime():
	image_names = os.listdir('static/images')
	return render_template("realtime.html", image_names=image_names)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
	image_names = os.listdir('static/detcc')
	if request.method == 'POST' and 'photo' in request.files:
		filename = photos.save(request.files['photo'])
		return filename
	return render_template('upload.html', image_names=image_names)

if __name__ == "__main__":
	app.run(host='192.168.43.81', port=5000, debug=True)