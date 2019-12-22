import cv2
import torch
import torch.nn as nn
import torchvision.transforms as transforms
import numpy as np

output_dim = 10

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

PATH = "./models/cnn_test.pt"
model.load_state_dict(torch.load(PATH))
model.eval()

def predict_mnist(im):

    size = 28
    # im = Image.open("/Users/bayartsogtyadamsuren/Public/Document_backup/NMIT/image-processing/image-processing-labs/end-project/tsogoo/final_project_mnist/mnist/template/static/public/img.png")
    # im = im.resize((28, 28))
    im = cv2.resize(im, (size, size), interpolation = cv2.INTER_AREA)

    im = np.array(im)[...,3]
    # for NN (making it (1, 28^2))
    test_tensor = torch.tensor(im.reshape(1, 1, 28, 28), dtype=torch.float32)

    pred = model(test_tensor)
    # print(pred)
    pred_ids = pred.argmax(1)
    print(pred_ids)

    return pred_ids.item()


