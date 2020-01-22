import cv2
import torch
import torch.nn as nn
import torchvision.transforms as transforms
import numpy as np

output_dim = 2

model = nn.Sequential(
    nn.Conv2d(in_channels=1, out_channels=3, kernel_size=5, stride=1, padding=0),
    nn.MaxPool2d(kernel_size=2),
    nn.ReLU(), # activation
    
    nn.Conv2d(in_channels=3, out_channels=5, kernel_size=4, stride=1, padding=0),
    nn.MaxPool2d(kernel_size=2),
    nn.ReLU(), # activation
    
    nn.Flatten(),
    nn.Linear(80, output_dim), # activation
    nn.Softmax()
)

PATH = "./model/cnn_model.pt"
model.load_state_dict(torch.load(PATH))
model.eval()

def predict(filename):
    im = cv2.imread(filename)
    size = 28
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
    predict = pred_ids.item()
    if(predict==0):
        predict="том хүн"
    if(predict==1):
        predict="хүүхэд"
    return predict
