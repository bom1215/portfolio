import numpy as np


def accuracy(y_true, y_pred):
    sample_size = y_true.shape[0]
    correct_size = (np.argmax(y_pred, axis=1) == np.argmax(y_true, axis=1)).sum()

    return correct_size / sample_size