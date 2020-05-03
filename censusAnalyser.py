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

    def __init__(self, censusdatafile):
        target_path =  os.path.join(os.path.dirname(__file__), censusdatafile)
        print(target_path)
        return pd.read_csv(target_path)

class StateCodeAnalyser:
    
    '''

    Create a StateCodeAnalyser class to load the State code CSV Data

    '''

    def __init__(self, statefile):
        target_path =  os.path.join(os.path.dirname(__file__), statefile)
        print(target_path)
        self.stateCode = pd.read_csv(target_path)
        return self.stateCode



class CSVStateCensus(StateCensusAnalyser,StateCodeAnalyser):
    
    '''

    Create CSVStateCensusClass to load the CSV Data

    '''
    
    def __init__(self):
        pass
    '''

    Check with StateCensusAnalyserto ensure number of record matches

    '''
    def getNumberofrecordes_censusdata(self,censusdatafile):
        self.csv_data = StateCensusAnalyser.__init__(self,censusdatafile)
        return len(self.csv_data)

    def getNumberofrecordes_statecode(self,statecodefile):
        self.stateCode = StateCodeAnalyser.__init__(self,statecodefile)
        return len(self.stateCode)

if __name__ == "__main__" :

    correctFilepath = 'StateCensusData.csv'
    wrongFilepath = 'StateCode.csv'
    Sca = CSVStateCensus()
    # print(CSVStateCensus().mro())
    print(Sca.getNumberofrecordes_censusdata(correctFilepath))
    print(Sca.getNumberofrecordes_statecode(statecodefile=wrongFilepath))