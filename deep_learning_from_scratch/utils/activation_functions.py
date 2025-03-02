import numpy as np

class Sigmoid:
    def __init__(self):
        # Variable to store the computed value from forward propagation
        self.x = None
        self.y = None

    def forward(self, x):
        '''
        Forward pass: Applies the sigmoid function
        
        Input: x (scalar or np.array) - Input data
        Output: y (scalar or np.array) - Result after applying the sigmoid function
        '''
        y = 1 / (1 + np.exp(-x))  # Compute the sigmoid function
        self.y = y  # Store for use in backpropagation
        self.x = x

        return y
    
    def backward(self, dt):
        '''
        Backward pass: Computes the gradient of the sigmoid function
        
        Input: dt (scalar or np.array) - Gradient propagated from the next layer
        Output: dx (scalar or np.array) - Gradient with respect to input
        '''
        
        return dt * self.y * (1 - self.y)  # Compute derivative of sigmoid (element-wise product)
class Relu:
    def __init__(self):
        # Variables to store input and output values
        self.y = None
        self.x = None
    
    def forward(self, x):
        '''
        Forward pass: Applies the ReLU function
        
        Input: x (scalar or np.array) - Input data
        Output: y (scalar or np.array) - Result after applying ReLU
        '''
        self.y = max(0, x)  # Compute ReLU
        self.x = x  # Store input for backpropagation
        return self.y
    
    def backward(self, dt):
        '''
        Backward pass: Computes the gradient of the ReLU function
        
        Input: dt (scalar or np.array) - Gradient propagated from the next layer
        Output: dx (scalar or np.array) - Gradient with respect to input
        '''
        dy = 1 if self.x > 0 else 0  # Compute derivative of ReLU
        return dt * dy
