import numpy as np
from deep_learning_from_scratch.utils.activation_functions import Sigmoid
from deep_learning_from_scratch.utils.loss_functions import SoftMaxWithCEE
from deep_learning_from_scratch.utils.layers import Affine


class Two_Layer_MLP:
    def __init__(self, input_size, hidden_size, output_size):
        self.x_train = None
        self.y_train = None
        self.params = {
            "w1": np.random.randn(input_size, hidden_size)
            / np.sqrt(input_size),  # Xavier initialization
            "w2": np.random.randn(hidden_size, output_size)
            / np.sqrt(hidden_size),  # Xavier initialization
            "b1": np.zeros(hidden_size),
            "b2": np.zeros(output_size),
        }
        self.grads = {"w1": None, "w2": None, "b1": None, "b2": None}
        self.loss = None

        self.input_layer = None
        self.activation_layer = None
        self.output_layer = None
        self.softmax_with_cee = None

    def forward(self):
        self.input_layer = Affine()
        self.activation_layer = Sigmoid()
        self.output_layer = Affine()
        self.softmax_with_cee = SoftMaxWithCEE()
        output1 = self.input_layer.forward(
            self.x_train, self.params["w1"], self.params["b1"]
        )
        output2 = self.activation_layer.forward(output1)  # => (100,50)
        output3 = self.output_layer.forward(
            output2, self.params["w2"], self.params["b2"]
        )

        predict = self.softmax_with_cee.forward(output3, self.y_train)  # => (50,10)

        return predict

    def loss_func(self):
        self.loss = self.softmax_with_cee.loss
        return self.loss

    def backward(self):

        dt = self.softmax_with_cee.backward()
        dt = self.output_layer.backward(dt)
        dt = self.activation_layer.backward(dt)
        dt = self.input_layer.backward(dt)

        self.grads["w1"] = self.input_layer.dw
        self.grads["b1"] = self.input_layer.db
        self.grads["w2"] = self.output_layer.dw
        self.grads["b2"] = self.output_layer.db

    def inference(self, x_test):
        input_layer = Affine()
        activation_layer = Sigmoid()
        output_layer = Affine()
        softmax_with_cee = SoftMaxWithCEE()

        output1 = input_layer.forward(x_test, self.params["w1"], self.params["b1"])
        output2 = activation_layer.forward(output1)
        output3 = output_layer.forward(output2, self.params["w2"], self.params["b2"])
        predict = softmax_with_cee.softmax(output3)

        return predict
