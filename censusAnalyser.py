import pandas as pd
import pathlib
from path import Path
import csv
import os
from censusAnalyserException import *

class StateCensusAnalyser:
    '''

    Create a StateCensusAnalyserClass to load the State Census CSV Data

    '''

    def __init__(self, filename):
        target_path_1 =  os.path.join(os.path.dirname(__file__), filename)
        print(target_path_1)
        return pd.read_csv(target_path_1)


class CSVStateCensus(StateCensusAnalyser):
    
    '''

    Create CSVStateCensusClass to load the CSV Data

    '''
    def __init__(self, filename):
        try:
            self.csv_data = super().__init__(filename)
        except FileNotFoundError:
            raise CensusException

    '''

    Check with StateCensusAnalyserto ensure number of record matches

    '''
    def getNumberofrecordes(self):
        return len(self.csv_data)
    

if __name__ == "__main__" :

    correctFilepath = 'StateCensusData.csv'
    wrongFilepath = 'StateCensusData1.csv'
    Sca = CSVStateCensus(filename=correctFilepath)
    print(Sca.getNumberofrecordes())
