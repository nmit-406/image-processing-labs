### SIMPLE FLASK APP FOR DIGIT RECOGNIZER ###

from flask import Flask, render_template, jsonify, make_response, request
from flask_restful import Resource, Api
import re
import os
import cv2
import numpy as np
import base64
from io import StringIO
from PIL import Image
from time import time


# local import
from predictor.nn_mnist import predict_mnist
# from flask_cors import CORS

app = Flask(__name__, static_folder='./template/static', template_folder='./template')
# CORS(app)

api = Api(app)

global current_img
global current_label

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

class MNIST(Resource):
    def get(self):
        return 'get'

    def post(self):
        print('coming here')
        

        # print(request.form)
        img = request.form.get("img")
        img = img.split(',')[1]
        
        img = base64.b64decode(img)

        np_data = np.fromstring(img,np.uint8)
        img = cv2.imdecode(np_data,cv2.IMREAD_UNCHANGED)
        
        prediction = predict_mnist(img)

        timestamp = time()
        cv2.imwrite(f'./users_choice/img-{timestamp}.png', img)

        return make_response(jsonify({'prediction': prediction, 'timestamp': timestamp}))

class CorrectOrWrong(Resource):
    def get(self):
        print('get')

    def post(self):
        print('is prediction?')
        print(request.form.get("correct_or_wrong"))
        itis = request.form.get("correct_or_wrong")
        timestamp = request.form.get("timestamp")
        prediction = request.form.get("prediction")

        folder = 'correct' if itis == 'true' else 'wrong'
        print(folder)
        os.replace(f'./users_choice/img-{timestamp}.png', f'./users_choice/{folder}/{prediction}-{timestamp}.png')
        print('saved!')
        # return 'post'

api.add_resource(MNIST, '/mnist')
api.add_resource(CorrectOrWrong, '/correct_or_wrong')

if __name__ == '__main__':
    app.run(debug=True)
