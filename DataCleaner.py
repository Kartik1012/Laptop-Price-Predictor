from hashlib import new
import pandas as pd
import numpy as np



class DataCleaner():
    def __init__(self, data):
        self.data = data

    def cutter(self, place_holder, n=1, sep=" "):
        new_data = []

        for i in self.data[place_holder]:
            i = i.split(sep)

            for x in range(n):
                i.pop(-1)


            i = int("".join(i))
            new_data.append(i)

        

        self.data[place_holder] = new_data
      

        return self.data


    def object_to_number(self, *place_holders):


        def make_it_happen( place_holder):

            unique_place_holders = []
            place_holders_index_relation = {}

            new_data = []
        

            for unique in self.data[place_holder].unique():
                unique_place_holders.append(unique)

                for item in unique_place_holders:
                    place_holders_index_relation[item] = unique_place_holders.index(item)

            for i in self.data[place_holder]:
                new_data.append(place_holders_index_relation.get(i))
                
            self.data[place_holder] = new_data
               
            return self.data


        for item in place_holders:
            make_it_happen(place_holder=item)
        
        return self.data



