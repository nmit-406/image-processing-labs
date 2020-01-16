import cv2
import torch
import torch.nn as nn
import numpy as np
import tensorflow as tf
import json
import matplotlib.pyplot as plt

class Predict:
    def shalgah(self,img):
        def conv2d(x, W, b, strides = 1):
            x = tf.nn.conv2d(x, W, strides = [1, strides, strides, 1], padding='SAME')
            x = tf.nn.bias_add(x, b)
            return tf.nn.relu(x)
        def maxpool2d(x, k=2):
            return tf.nn.max_pool(x, ksize = [1, k, k, 1], strides = [1, k, k, 1], padding = 'SAME')
        def neural_network(x, weight, bias, dropout):
            x = tf.reshape(x, shape = [-1, 28, 28, 1])

            conv1 = conv2d(x, weight['w1'], bias['b1']) # Convolutional Layer 1
            conv1 = maxpool2d(conv1) # Pooling Layer 1

            conv2 = conv2d(conv1, weight['w2'], bias['b2']) # Convolutional Layer 1
            conv2 = maxpool2d(conv2) # Pooling Layer 1

            # Fully Connected Layer 1
            # Reshaping output of previous convolutional layer to fit the fully connected layer
            fc = tf.reshape(conv2, [-1, weights['w3'].get_shape().as_list()[0]])
            fc = tf.add(tf.matmul(fc, weight['w3']), bias['b3']) # Linear Function
            fc = tf.nn.relu(fc) # Activation Function

            fc = tf.nn.dropout(fc, dropout) # Applying dropout on Fully Connected Layer

            out = tf.add(tf.matmul(fc, weight['w4']), bias['b4']) # Output Layer
            return out
        def get_prediction(img):
            with tf.Session() as sess:
                pred = sess.run(y_pred, feed_dict = { X1 : img, keep_prob : 1.0 })
            pred = list(pred.flatten())
            pred = pred.index(max(pred))*20
            return pred
        X1 = tf.placeholder(tf.float32, shape = [None, 784]) # Placeholder for Feature Matrix
        Y2 = tf.placeholder(tf.float32, shape = [None, 6]) # Placeholder for Labels
        keep_prob = tf.placeholder(tf.float32) 
        weights = {
            'w1' : tf.convert_to_tensor(np.array(np.load('w1.npy')),dtype=tf.float32),
            'w2' : tf.convert_to_tensor(np.array(np.load('w2.npy')),dtype=tf.float32),
            'w3' : tf.convert_to_tensor(np.array(np.load('w3.npy')),dtype=tf.float32),
            'w4' : tf.convert_to_tensor(np.array(np.load('w4.npy')),dtype=tf.float32)
        }
        biases = {
            'b1' : tf.convert_to_tensor(np.array(np.load('b1.npy')),dtype=tf.float32),
            'b2' : tf.convert_to_tensor(np.array(np.load('b2.npy')),dtype=tf.float32),
            'b3' : tf.convert_to_tensor(np.array(np.load('b3.npy')),dtype=tf.float32),
            'b4' : tf.convert_to_tensor(np.array(np.load('b4.npy')),dtype=tf.float32)
        }
        y_pred = neural_network(X1, weights, biases, 1.0)
        img = cv2.resize(img,(28,28))
        img=img.flatten()
        img = torch.tensor(img)
        pred = get_prediction(img.reshape(1, 784))
        return pred
