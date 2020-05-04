import pandas as pd
import pathlib
from path import Path
import csv
import os
import json
from censusAnalyserException import *
from pandas.errors import ParserWarning,ParserError

class StateCensusAnalyser:
    '''

    Create a StateCensusAnalyserClass to load the State Census CSV Data

    '''

    def __init__(self, censusdatafile):
        try:

            __target_path =  os.path.join(os.path.dirname(__file__), censusdatafile)
            # print(__target_path)
            return pd.read_csv(__target_path,delimiter=',', engine='python')
        except FileNotFoundError as e:
            raise FileTypeNotCorrectException
        

class StateCodeAnalyser:

    '''

    Create a StateCodeAnalyser class to load the State code CSV Data

    '''

    def __init__(self, statefile):
        try:
            
            __target_path =  os.path.join(os.path.dirname(__file__), statefile)
            # print(__target_path)
            return pd.read_csv(__target_path,delimiter=',')

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
            print(type(self.__csv_data))
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

    '''

    Use Iterator to load the data

    '''

    def iterator(self,filename):
        '''

        I guess. If you may only run a function very rarely and don't need the module imported anywhere else, 
        it may be beneficial to only import it in that function

        '''
        from itertools import zip_longest as zip
        infile = csv.reader(open(filename))

        #This skips the first row of the CSV file
        next(infile)

        transposed = zip(*infile)
        iterator_list = []
        for c in transposed:
            iterator_list.append(c)
        return iterator_list

class __StateSensusHandler(_CSVStateCensus):

    def __init__(self, *args, **kwargs):
        pass

    '''
    Save the State Census Data into a Json File
    '''

    def to_stateCensusjsondata(self,__filename):
        self.__csv_dataframe = StateCensusAnalyser.__init__(self,__filename)
        return self.__csv_dataframe.reset_index().to_json(r'StateCensusData.json',orient='records')
    
    def to_stateCodejsondata(self,__filename):
        self.__csv_dataframe = StateCodeAnalyser.__init__(self,__filename)
        return self.__csv_dataframe.reset_index().to_json(r'StateCodeJsondata.json',orient='records')
    
    
    
if __name__ == "__main__" :

    # if input('do u want to specify file (y or n)').__contains__(['y','Y']):
    #     correctFilepath = input('enter file name: ')
    __correctFilepath = 'StateCensusData.csv'
    __wrongFilepath = 'StateCode.csv'
    Sca = _CSVStateCensus()
    # print(__StateSensusHandler.mro())
    # print(Sca.getNumberofrecordes_censusdata(__correctFilepath))
    # print(Sca.getNumberofrecordes_statecode(__wrongFilepath))
    # # print(Sca.to_jsondata(__correctFilepath))
    # print(Sca.iterator(__correctFilepath))
    __StateSensusHandler().to_stateCensusjsondata(__wrongFilepath)
    __StateSensusHandler().to_stateCodejsondata(__correctFilepath)