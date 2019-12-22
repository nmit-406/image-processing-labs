# Tsogoo's final project: MNIST using CNN and NN

![mnist demo][demo]

[demo]: https://raw.githubusercontent.com/nmit-406/image-processing-labs/master/end-project/tsogoo/final_project_mnist/mnist/images/nmit-img-processing-demo-5.gif "Demo gif"

This is the Flask based application and CNN model working behind the back-end using inference of the model.

Project is tested in python3.6.x, but not python2.x.x versions

This README currently includes:
- How To Work
- Further Improvements
- References

### How To Work

Run following commands to start the back-end server
```
git clone https://github.com/nmit-406/image-processing-labs.git # if you did not clone
cd end-project/tsogoo/final_project_mnist/mnist/
pip install -r requirement.txt
python app.py
```


Open your browser and copy the link below
```
http://localhost:5000
```

### Further Improvements

- Current model is not good enough because of its a lack of data. So collecting more data and automatic training using batch-process should be done.
- This demo only works for the browser not for the mobile phone versions. This is the other direction to develop

### References

- [ImageNet Classification with Deep Convolutional Neural Networks by Alex Krizhevsky, Ilya Sutskever, and Geoffrey E. Hinton](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf)
- [MNIST dataset from Kaggle](https://www.kaggle.com/c/digit-recognizer)
