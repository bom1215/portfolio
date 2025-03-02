#
# This is a sample Notebook to demonstrate how to read "MNIST Dataset"
# https://www.kaggle.com/code/hojjatk/read-mnist-dataset
#
import numpy as np # linear algebra
import struct
from array import array
from os.path  import join
import matplotlib.pyplot as plt
import random

#
# MNIST Data Loader Class
#
class MnistDataloader(object):
    def __init__(self, training_images_filepath,training_labels_filepath,
                 test_images_filepath, test_labels_filepath):
        
        
        self.training_images_filepath = training_images_filepath
        self.training_labels_filepath = training_labels_filepath
        self.test_images_filepath = test_images_filepath
        self.test_labels_filepath = test_labels_filepath
    
    def read_images_labels(self, images_filepath, labels_filepath):        
        labels = []
        with open(labels_filepath, 'rb') as file:
            magic, size = struct.unpack(">II", file.read(8))
            if magic != 2049:
                raise ValueError('Magic number mismatch, expected 2049, got {}'.format(magic))
            labels = array("B", file.read())        
        
        with open(images_filepath, 'rb') as file:
            magic, size, rows, cols = struct.unpack(">IIII", file.read(16))
            if magic != 2051:
                raise ValueError('Magic number mismatch, expected 2051, got {}'.format(magic))
            image_data = array("B", file.read())        
        images = []
        for i in range(size):
            images.append([0] * rows * cols)
        for i in range(size):
            img = np.array(image_data[i * rows * cols:(i + 1) * rows * cols])
            img = img.reshape(28, 28)
            images[i][:] = img            
        
        return images, labels
    
    def one_hot_handling(self, arr, label_nums):
        return np.identity(label_nums)[arr]
        
            
    def load_data(self, one_hot = True):
        x_train, y_train = self.read_images_labels(self.training_images_filepath, self.training_labels_filepath)
        x_test, y_test = self.read_images_labels(self.test_images_filepath, self.test_labels_filepath)
        if one_hot:
            y_train = self.one_hot_handling(y_train, 10)
            y_test = self.one_hot_handling(y_test, 10)
        return (x_train, y_train),(x_test, y_test) 
      
    
    def show_random_data(self, x_train, x_test, y_train, y_test):
        # Show some random training and test images 
        
        images_2_show = []
        titles_2_show = []
        for i in range(0, 10):
            r = random.randint(1, 60000)
            images_2_show.append(x_train[r])
            titles_2_show.append('training image [' + str(r) + '] = ' + str(np.argmax(y_train[r])))

        for i in range(0, 5):
            r = random.randint(1, 10000)
            images_2_show.append(x_test[r])        
            titles_2_show.append('test image [' + str(r) + '] = ' + str(np.argmax(y_test[r])))

        self.show_images(images_2_show, titles_2_show)
    
    def show_images(self,images, title_texts):
        cols = 5
        rows = int(len(images)/cols) + 1
        plt.figure(figsize=(30,20))
        index = 1    
        for x in zip(images, title_texts):        
            image = x[0]        
            title_text = x[1]
            plt.subplot(rows, cols, index)        
            plt.imshow(image, cmap=plt.cm.gray)
            if (title_text != ''):
                plt.title(title_text, fontsize = 15);        
            index += 1
    


    