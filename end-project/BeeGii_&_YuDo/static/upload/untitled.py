from mtcnn.mtcnn import MTCNN
import cv2
import json
detector = MTCNN()
for zurag in range(16,18):
    img = cv2.imread("test/img"+str(zurag)+".jpg")
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
    cv2.imwrite("test/img"+str(zurag)+".jpg",crop_img)
  
