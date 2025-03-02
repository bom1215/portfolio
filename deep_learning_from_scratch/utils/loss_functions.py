import numpy as np


class SoftMaxWithCEE:
    def __init__(self):
        self.y_pred = None 
        self.y_true = None # one-hot vector
        self.loss = None

    def softmax(self, x):
        c = np.max(x)
        numerator = np.exp(x-c)  # overflow 방지
        denumerator = np.sum(np.exp(x-c), axis=-1).reshape(-1,1) # 열기준 합산
        self.y_pred = numerator / denumerator

        return self.y_pred

    def CEE(self, y_true, y_pred): 
        # Cross Entropy Error

        self.y_true = y_true
        delta = 1e-7 # To prevent np.log(0)

        return np.mean(-np.sum(y_true * np.log(y_pred + delta), axis=1)) # # 배치 크기로 평균
    
    def forward(self,x, y_true):
        y_pred = self.softmax(x)
        self.loss =  self.CEE(y_true, y_pred)

        return self.loss

    def backward(self, dt=1):
        
        batch_size = self.y_pred.shape[0]
        dx = (self.y_pred - self.y_true) / batch_size
        return dt * dx