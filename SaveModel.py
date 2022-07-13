from operator import mod
import pickle

class ModelSaver():
    def save(self, my_model):
        with open("savedmodel.pickle", "wb") as f:
            pickle.dump(my_model, f)

    def load(self):
        pickle_in = open("savedmodel.pickle", "rb")
        my_model = pickle.load(pickle_in)
        return my_model