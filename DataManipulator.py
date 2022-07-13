from pandas import period_range
import sklearn
import numpy as np
from sklearn import linear_model
from sklearn.utils import shuffle


class DataManipulator():
    def __init__(self, data):
        self.data = data
        self.x_train = 0
        self.x_test = 0
        self.y_train = 0
        self.y_test = 0

    def splitter(self, predict, sample_size):
        x = np.array(self.data.drop([predict], 1))
        y = np.array(self.data[predict])

        self.x_train, self.x_test, self.y_train, self.y_test = sklearn.model_selection.train_test_split(x, y, test_size=sample_size)

    def x_train_dp(self):
        return self.x_train

    def x_test_dp(self):
        return self.x_test

    def y_train_dp(self):
        return self.y_train

    def y_test_dp(self):
        return self.y_test