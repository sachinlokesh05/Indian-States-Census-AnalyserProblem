import pandas as pd
import csv
import os
class StateCensusAnalyser:
    
    def __init__(self, filename):
        target_path_1 = os.path.join(os.path.dirname(__file__), filename)
        self.csv_data = csv.DictReader(open(target_path_1,mode='r'))
        self.csv_data1=pd.read_csv(target_path_1)


class CSVStateCensus(StateCensusAnalyser):
    
    def __init__(self, filename):
        self.a = super().__init__(filename)
    def do_something(self):
        df_dict=self.csv_data1.to_dict()
        print(df_dict['State name'])
        #count number of rows
        print(df_dict.__len__())

if __name__ == "__main__" :

    Sca = CSVStateCensus(filename='indian_census_data_2011.csv')
    Sca.do_something()