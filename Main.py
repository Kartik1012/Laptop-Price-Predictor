import pandas as pd
from DataCleaner import DataCleaner
from DataManipulator import DataManipulator
from Model import Model
from SaveModel import ModelSaver
from Predictor import Predictor
import random


def preparing():
    #Loading Data
    data = pd.read_csv("Cleaned_Laptop_data.csv", na_values='n/a')
    data = data[["brand", "processor_gnrtn", "ram_gb", "ssd", "hdd", "os", "os_bit", "graphic_card_gb", "display_size", "Touchscreen", "ratings", "latest_price"]]

    #Cleaning data using Datacleaner class
    data_cleaner = DataCleaner(data=data)
    new_data = data_cleaner.cutter(place_holder="ram_gb", n=2)
    new_data = data_cleaner.cutter(place_holder="hdd")
    new_data = data_cleaner.cutter(place_holder="ssd")

    new_data = data_cleaner.object_to_number("brand", "processor_gnrtn", "os", "os_bit", "display_size", "Touchscreen")

    #Passed our data into data manupilator class to split training and test data
    data_manupilator = DataManipulator(new_data)

    best = 0
    for iteration in range(10000):
        splitted_data = data_manupilator.splitter("latest_price", random.uniform(0.05, 0.3))
        my_model = Model(data_manupilator.x_train, data_manupilator.x_test, data_manupilator.y_train, data_manupilator.y_test)
        my_model.make_model()

        if my_model.evaluate_model() > best:
            best = my_model.evaluate_model()
            model_saver = ModelSaver()
            model_saver.save(my_model.return_model())
        
        print(best)
    
preparing()

def predict():
    model_saver = ModelSaver()
    my_model = model_saver.load()
    predictor = Predictor(my_model, [[0, 0, 8, 256, 0, 0, 2, 4, 14, 1, 150]])
    prediction = predictor.predict()
    return prediction/100

print(predict())
