from mtcnn.mtcnn import MTCNN
import cv2
import json

class Tsarai:
    def tanih(self,img):
        try:
            detector = MTCNN()
            box = detector.detect_faces(img)
            y = box[0]['box'][1]
            x = box[0]['box'][0]
            if x<0:
                x=0
            if y<0:
                y=0
            h = box[0]['box'][3]
            w = box[0]['box'][2]
        except IndexError:
            return img
        return img[y:y+h, x:x+w]
        
  
