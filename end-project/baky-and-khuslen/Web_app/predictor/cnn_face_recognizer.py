import cv2
import torch
import torch.nn as nn
import numpy as np

output_dim = 10

model = nn.Sequential(
    nn.Conv2d(in_channels=1, out_channels=4, kernel_size=8, stride=1, padding=0),
    nn.MaxPool2d(kernel_size=4),
    nn.ReLU(), # activation
    
    nn.Conv2d(in_channels=4, out_channels=16, kernel_size=5, stride=1, padding=0),
    nn.MaxPool2d(kernel_size=2),
    nn.ReLU(), # activation
    
    nn.Conv2d(in_channels=16, out_channels=25, kernel_size=3, stride=1, padding=0),
    nn.MaxPool2d(kernel_size=2),
    nn.ReLU(), # activation
    
    nn.Flatten(),
    nn.Linear(3025, 3), # activation
    nn.Softmax(dim= None)
)

PATH = "./models/cnn_khuslen_baky.pt"
model.load_state_dict(torch.load(PATH))
model.eval()

def predict_face(filename):
    im = cv2.imread(filename)
    size = 224
    # print(im)
    im = cv2.resize(im, (size, size))
    print (im.shape)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    test_tensor = torch.tensor(im, dtype=torch.float32).unsqueeze(0)
    test_tensor = test_tensor.unsqueeze(0)
    pred = model(test_tensor)
    # print(pred)
    pred_ids = pred.argmax(1)
    print(pred_ids)
    recognized_as ="aaa"
    recognized_as = pred_ids.item()
    if(recognized_as==0):
        recognized_as="khuslen"
    if(recognized_as==1):
        recognized_as="baky"
    if(recognized_as==2):
        recognized_as="other"
    return recognized_as


