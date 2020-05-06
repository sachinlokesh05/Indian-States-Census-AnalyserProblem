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
        
    def __str__(self):
        return str(self.__class__)

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

    def __str__(self):
        return str(self.__class__)

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
        import inspect

    '''
    Save the State Census Data into a Json File
    '''

    def __to_stateCensusjsondata(self,__filename):
        self.__censusdataframe = StateCensusAnalyser.__init__(self,__filename)
        sortedStatecesusData = self.__sort_statesDataInAlphabeticalOrdertojsonfile(self.__censusdataframe)
        return sortedStatecesusData.reset_index().to_json(r'StateCensusJsonData.json',orient='records')
    
    def __to_stateCodejsondata(self,__filename):
        self.__statecodedataframe = StateCodeAnalyser.__init__(self,__filename)
        sortedStatecodeData = self.__sort_statesDataInAlphabeticalOrdertojsonfile(self.__statecodedataframe)
        return sortedStatecodeData.reset_index().to_json(r'StateCodeJsondata.json',orient='records')
    
    def Sorting_statesCensusDataInAlphabeticalOrder(self):
        print('State Census Data')
        return self.sort_statesDataInAlphabeticalOrder(self.__censusdataframe).to_json()

    def Sorting_statesCodeDataInAlphabeticalOrder(self):
        print('State Code Data')
        return self.sort_statesDataInAlphabeticalOrder(self.__statecodedataframe).to_json()

    '''

    Create a Sorting function in the Analyser to
    Sort the States in the alphabetical order

    '''
    def sort_statesDataInAlphabeticalOrder(self,data):
        '''

        With the python module inspect, one can inspect (not kidding) the run-time python stack. 
        Among other things, this makes it possible to get the name of the current function or callers. Handy for logging or debugging purposes. 

        '''
        
        if inspect.stack()[1][3]  is 'Sorting_statesCensusDataInAlphabeticalOrder' :
            return data.sort_values(by=['State'])
        elif inspect.stack()[1][3]  is 'Sorting_statesCodeDataInAlphabeticalOrder' :
            return data.sort_values(by=['StateCode'])
        return 'check the method  again'
    
    def __sort_statesDataInAlphabeticalOrdertojsonfile(self,data):
        
        if inspect.stack()[1][3]  is '__to_stateCensusjsondata' :
            return data.sort_values(by=['DensityPerSqKm'])
        return 'check the method  again'

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
    __StateSensusHandler().to_stateCensusjsondata(__correctFilepath)
    __StateSensusHandler().to_stateCodejsondata(__wrongFilepath)