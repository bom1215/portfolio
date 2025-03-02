import numpy as np


def min_max_scale(x):
    return (x - np.min(x)) / (np.max(x) - np.min(x))