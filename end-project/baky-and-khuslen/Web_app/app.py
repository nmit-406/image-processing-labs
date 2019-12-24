import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from PIL import Image
import numpy as np

UPLOAD_FOLDER = './static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/upload_file', methods = ['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        fullFileName= os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(fullFileName)
        blur_image(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template('end.html',filename=fullFileName)
def blur_image(filename):
    im = np.array(Image.open(filename))
    data = np.asarray(im)
    kernel2d= np.array([[1.,4,6,4,1],[4,16,24,16,4],[6,24,36,24,6],[4,16,24,16,4],[1,4,6,4,1]])/256
    r,g,b =data[:,:,0],data[:,:,1], data[:,:,2]
    height = len(kernel2d)
    width = len(kernel2d[0])
    blurredr= np.copy(r)
    blurredg= np.copy(g)
    blurredb= np.copy(b)
    for i in range(len(r)-height+1):
        for j in range(len(r[0])-width+1):
            blurredr[i][j]=\
                np.sum(r[i:i+height, j:j+width]*kernel2d)
            blurredg[i][j]=\
                np.sum(g[i:i+height, j:j+width]*kernel2d)
            blurredb[i][j]=\
                np.sum(b[i:i+height, j:j+width]*kernel2d)
    blurred=np.dstack((blurredr,blurredg,blurredb))
    im = Image.fromarray(np.uint8(blurred))
    im.save(filename)
    return
app.run(debug = True)