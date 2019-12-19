### SIMPLE FLASK APP FOR DIGIT RECOGNIZER ###


from flask import Flask, render_template, jsonify, make_response, request
from flask_restful import Resource, Api
import re
import cv2
import numpy as np
# from flask_cors import CORS

app = Flask(__name__, static_folder='./template/static', template_folder='./template')
# CORS(app)

api = Api(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

# @app.route('/mnist/',methods = ['GET','POST'])
# def mnist():
#     if request.method =='POST':
#         return "post"


class MNIST(Resource):
    def get(self):
        return 'get'

    def post(self):
        print('coming here')
        print(request.data)
        data = str(request.data)
!!!!!!!!!!!!!!!!! aldaatai


        encoded_data = data.split(',')[1]
        nparr = np.fromstring(encoded_data.decode('base64'), np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        print(img.size())
        # print(len(request.files))
        # print(request.files['img'])
        # print('coming here')
        # img = request.files[0]
        # img.save('./static/img.png')
        return 'post'

api.add_resource(MNIST, '/mnist')

if __name__ == '__main__':
    app.run(debug=True)
