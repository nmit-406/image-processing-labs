from mtcnn.mtcnn import MTCNN
import cv2
import json
detector = MTCNN()
with open('image.json') as f:
  data = json.load(f)
for zurag in data['images']:
    try:
        img = cv2.imread("smiling/"+zurag['name'])
        box = detector.detect_faces(img)
        y = box[0]['box'][1]
        x = box[0]['box'][0]
        if x<0:
            x=0
        if y<0:
            y=0
        h = box[0]['box'][3]
        w = box[0]['box'][2]
        crop_img = img[y:y+h, x:x+w]
        cv2.imwrite("smiling/"+zurag['name'],crop_img)
    except IndexError:
        continue
