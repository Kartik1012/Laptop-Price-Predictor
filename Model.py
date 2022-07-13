from sklearn import linear_model
from sklearn.utils import shuffle
import pickle

class Model():
    def __init__(self, x_train, x_test, y_train, y_test):
        self.x_train = x_train
        self.x_test = x_test
        self.y_train = y_train
        self.y_test = y_test

        self.linear = linear_model.LinearRegression()

    def make_model(self):
        self.linear.fit(self.x_train, self.y_train)

    def evaluate_model(self):
        
        acc = self.linear.score(self.x_test, self.y_test)

        return acc
    
    def return_model(self):
        return self.linear
