import cv2
import torch
import torch.nn as nn
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np

model = nn.Sequential(
            nn.Linear(784,300), # nn.conv2d(in_channel=1, out_channel=3, kernel_size=5, stride=1, padding=1) #narrow vs same
            # nn.MaxPool2d()
            nn.ReLU(),
            nn.Linear(300,100), #
            nn.ReLU(),
            nn.Linear(100,10),  #
            nn.Softmax()
        )

PATH = "./models/naive_nn.pt"
model.load_state_dict(torch.load(PATH))
model.eval()

def predict_mnist(im):

    size = 28
    # im = Image.open("/Users/bayartsogtyadamsuren/Public/Document_backup/NMIT/image-processing/image-processing-labs/end-project/tsogoo/final_project_mnist/mnist/template/static/public/img.png")
    # im = im.resize((28, 28))
    im = cv2.resize(im, (size, size), interpolation = cv2.INTER_AREA)

    im = np.array(im)[...,3]
    # for NN (making it (1, 28^2))
    test_tensor = torch.tensor(im.reshape(1, size ** 2), dtype=torch.float32)

    pred = model(test_tensor)
    # print(pred)
    pred_ids = pred.argmax(1)
    print(pred_ids)

    return pred_ids.item()


