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
        try:

            __target_path =  os.path.join(os.path.dirname(__file__), censusdatafile)
            print(__target_path)
            return pd.read_csv(__target_path,delimiter=';')
            
        except FileNotFoundError as e:
            raise FileTypeNotCorrectException

class StateCodeAnalyser:

    '''

    Create a StateCodeAnalyser class to load the State code CSV Data

    '''

    def __init__(self, statefile):
        try:
            
            __target_path =  os.path.join(os.path.dirname(__file__), statefile)
            print(__target_path)
            return pd.read_csv(__target_path)

        except FileNotFoundError as e:
            raise FileTypeNotCorrectException


class _CSVStateCensus(StateCensusAnalyser,StateCodeAnalyser):
    
    '''

    Create CSVStateCensusClass to load the CSV Data

    '''
    
    def __init__(self):
        pass
    '''

    Check with StateCensusAnalyserto ensure number of record matches

    '''
    def getNumberofrecordes_censusdata(self,__censusdatafile):
        self.__csv_data = 0
        try:
            self.__csv_data = StateCensusAnalyser.__init__(self,__censusdatafile)
        except FileNotFoundError :
            raise FileNotCorrectException
        return len(self.__csv_data)

    def getNumberofrecordes_statecode(self,__statecodefile):
        self.__statecode = 0
        try:
            self.__statecode = StateCodeAnalyser.__init__(self,__statecodefile)
        except FileNotFoundError :
            raise FileNotCorrectException
        return len(self.__statecode)

if __name__ == "__main__" :

    # if input('do u want to specify file (y or n)').__contains__(['y','Y']):
    #     correctFilepath = input('enter file name: ')
    __correctFilepath = 'StateCensusData.csv'
    __wrongFilepath = 'StateCode.csv'
    Sca = _CSVStateCensus()
    # print(CSVStateCensus().mro())
    print(Sca.getNumberofrecordes_censusdata(__correctFilepath))
    print(Sca.getNumberofrecordes_statecode(__wrongFilepath))