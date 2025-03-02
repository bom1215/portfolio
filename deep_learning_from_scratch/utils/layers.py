
import numpy as np


class Affine:
    def __init__(self):
        self.x = None
        self.y = None
        self.bias = None
        self.weight = None
        self.dw = None
        self.db = None


    def forward(self,x, weight, bias):
        self.x = x
        self.weight = weight
        self.bias = bias
        self.y =  np.dot(self.x,  self.weight) + self.bias
        return self.y
    
    def backward(self, dt):
        dx = np.dot(dt, np.transpose(self.weight))
        self.dw = np.dot(np.transpose(self.x), dt)
        self.db = np.sum(dt, axis= 0)
        return dx
