import pandas as pd
import pathlib
from path import Path
import csv
import os
class StateCensusAnalyser:
    
    def __init__(self, filename):
        target_path_1 =  os.path.join(os.path.dirname(__file__), filename)
        print(target_path_1)
        return pd.read_csv(target_path_1)


class CSVStateCensus(StateCensusAnalyser):
    
    def __init__(self, filename):
        self.csv_data = super().__init__(filename)
        
    def getNumberofrecordes(self):
        return len(self.csv_data)
        
    

if __name__ == "__main__" :

    Sca = CSVStateCensus(filename='StateCensusData.csv')
    print(Sca.getNumberofrecordes())
