




class Predictor():
    def __init__(self, model, values):
        self.model = model
        self.values = values

    def predict(self):
        return self.model.predict(self.values)