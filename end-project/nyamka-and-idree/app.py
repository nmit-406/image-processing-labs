from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
from PIL import Image
import numpy as np



app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


# app.config	['SQLALCHEMY_DATABASE_URI']= 'sqlite:///test.db'
# db = SQLAlchemy(app)

# class Todo(db.Model):
# 	id = db.Column(db.Integer, primary_key = True)
# 	image = db.Column(db.LargeBinary)
# 	def __repr__(self):
# 		return '<Images %r>' % self.id
@app.route('/')
def index():
	return render_template('index.html')
@app.route('/upload',methods=['POST'] )
def upload():
	dir = os.path.join(APP_ROOT, 'static/')
	if not os.path.isdir(dir):
		os.mkdir(dir)
	for upload in request.files.getlist('file'):
		filename = upload.filename
		dest = "/".join([dir,filename])
		upload.save(dest)
	edetect_image(dest)
	return render_template("complete.html", image_name=filename)
# @app.route('/upload/<filename>')
# def send_image(filename):
# 	return send_from_directory('image', filename)

	# if 'image' not in request.files:
 #        flash('No file part')
 #        return redirect(request.url)
 #    file = request.files['image']
 #    if image.filename == '':
 #        flash('No selected file')
 #        return redirect(request.url)
 #    if image and allowed_file(image.filename):
 #        filename = secure_filename(image.filename)
 #        fullFileName= os.path.join(app.config['UPLOAD_FOLDER'], filename)
 #        file.save(fullFileName)
 #        # blur_image(os.path.join(app.config['UPLOAD_FOLDER'], filename))
 #        return render_template('complete.html')

def edetect_image(filename):
	im = np.array(Image.open(filename))
	data = np.asarray(im)
	ker2=np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])/256
	r,g,b =data[:,:,0],data[:,:,1], data[:,:,2]
	height = len(ker2)
	width = len(ker2[0])
	detectedr= np.copy(r)
	detectedg= np.copy(g)
	detectedb= np.copy(b)
	for i in range(len(r)-height+1):
		for j in range(len(r[0])-width+1):
			detectedr[i][j]=\
				np.sum(r[i:i+height, j:j+width]*ker2)
			detectedg[i][j]=\
				np.sum(g[i:i+height, j:j+width]*ker2)
			detectedb[i][j]=\
				np.sum(b[i:i+height, j:j+width]*ker2)
	detected=np.dstack((detectedr,detectedg,detectedb))
	im = Image.fromarray(np.uint8(detected))
	im.save(filename)
	return

if __name__ == "__main__":
	app.run(debug=True)