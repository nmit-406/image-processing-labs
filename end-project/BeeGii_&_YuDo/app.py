from flask import Flask, render_template, request, redirect, send_from_directory, jsonify,url_for
import os
import cv2
from Predict import Predict
from Tsarai import Tsarai
app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app.config["UPLOAD_FOLDER"] = os.path.join('static/','upload/')

@app.route('/')
def index():
    
    return render_template("index.html")


@app.route('/upload', methods = ['POST'])
def upload():

    target = "static/upload"
    
    if not os.path.isdir(target):
        os.mkdir(target)
    
    image = request.files['file']
    filename = image.filename
    
    destination = "/".join([target, filename])

    image.save(destination)

    destination2 = os.path.join(APP_ROOT,destination)
    img = cv2.imread(destination2)
    target = os.path.join(APP_ROOT,target)
    #tsaraig ni taniad crop hiih heseg
    b=Tsarai()
    img = b.tanih(img)
    #ineej baigaa esehiig tanih
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    a=Predict()
    #print(a.shalgah(img))
    
    return render_template('index.html',user_image = destination,imgname = image.filename, hariu = a.shalgah(img))

if __name__ == "__main__":
    app.run(debug=True)