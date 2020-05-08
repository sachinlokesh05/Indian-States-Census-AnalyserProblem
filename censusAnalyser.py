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
    
    def __init__(self, censusfilename,codefilename):
        global __censusdataframe 
        __censusdataframe = StateCensusAnalyser.__init__(self,censusfilename)
        global  __statecodedataframe
        __statecodedataframe = StateCodeAnalyser.__init__(self,codefilename)

    '''
    Save the State Census Data into a Json File
    '''

    def to_stateCensusjsondata(self):
        
        print(__censusdataframe)
        sortedStatecesusData = self.__sort_statesDataInAlphabeticalOrdertojsonfile(data=__censusdataframe)
        return sortedStatecesusData
    
    def to_stateCodejsondata(self):
        
        sortedStatecodeData = self.__sort_statesDataInAlphabeticalOrdertojsonfile(__statecodedataframe)
        return sortedStatecodeData

    def Sorting_statesCensusDataOnopulationDensity(self):
        return self.__sort_statesDataInAlphabeticalOrdertojsonfile(__censusdataframe)

    def Sorting_statesCensusDataOnArea(self):
        return self.__sort_statesDataInAlphabeticalOrdertojsonfile(__censusdataframe)

    '''

    Ability for Analyser to
    report the State Census
    Data in a Json Format
    according to State
    alphabetical order

    '''

    def Sorting_statesCensusDataInAlphabeticalOrder(self):
        # __censusdataframe = StateCensusAnalyser.__init__(self,__filename)
        return self.__sort_statesDataInAlphabeticalOrder(__censusdataframe).to_json()

    '''

    Ability for Analyser to
    report the State Census
    Data in a Json Format as
    per State Code in an
    alphabetical order

    '''

    def Sorting_statesCodeDataInAlphabeticalOrder(self):
        # __statecodedataframe = StateCodeAnalyser.__init__(self,__filename)
        return self.__sort_statesDataInAlphabeticalOrder(__statecodedataframe).to_json()
    
    def __sort_statesDataInAlphabeticalOrder(self,data):
        '''

        With the python module inspect, one can inspect (not kidding) the run-time python stack. 
        Among other things, this makes it possible to get the name of the current function or callers. Handy for logging or debugging purposes. 

        '''
        import inspect
        try:
            if inspect.stack()[1][3]  == 'Sorting_statesCensusDataInAlphabeticalOrder' :
                return data.sort_values(by=['State'])
            elif inspect.stack()[1][3]  == 'Sorting_statesCodeDataInAlphabeticalOrder' :
                return data.sort_values(by=['StateCode'])
            else:
                return "check the method again"

        except FileNotFoundError:
            FileNotCorrectException

        except FileExistsError :
            FileTypeNotCorrectException

    def __sort_statesDataInAlphabeticalOrdertojsonfile(self,data):
        import inspect

        try:
            '''
            Ability to report the State
            Census Data in a Json
            Format from most
            populous state to the
            least one
            '''
            if inspect.stack()[1][3]  == 'to_stateCensusjsondata' :
                return data.sort_values(by=['State'],ascending=False).reset_index().to_json(r'StateCensusJsonData.json',orient='records')

            '''
            Ability to report the
            State Census Data in a
            Json format from
            Largest State by DensityPerSqKm to
            the smallest state
            '''
            if inspect.stack()[1][3]  == 'Sorting_statesCensusDataOnArea' :
                return data.sort_values(by=['DensityPerSqKm'],ascending=False).reset_index().to_json(r'StateCensusSortedonPopulationDensity.json',orient='records')

            '''
            Ability to report the
            State Census Data in a
            Json format from
            Largest State by Area to
            the smallest state
            '''
            if inspect.stack()[1][3]  == 'Sorting_statesCensusDataOnArea' :
                return data.sort_values(by=['AreaInSqKm'],ascending=False).reset_index().to_json(r'StateCensusSortedonArea.json',orient='records')

            '''
            Ability to report the
            StateC ode Data in a
            Json File from most
            population density
            state to the least one
            '''
            if inspect.stack()[1][3]  == 'to_stateCodejsondata' :
                return data.sort_values(by=['StateCode']).reset_index().to_json(r'StateCodeJsondata.json',orient='records')

            else:
                return "check the method again"

        except FileNotFoundError :
            raise FileNotCorrectException

        except FileExistsError :
            raise FileTypeNotCorrectException

if __name__ == "__main__" :

    # if input('do u want to specify file (y or n)').__contains__(['y','Y']):
    #     correctFilepath = input('enter file name: ')
    __correctFilepath = 'StateCensusData.csv'
    __wrongFilepath = 'StateCode.csv'
    Sca = _CSVStateCensus()
    # print(__StateSensusHandler.mro())
    # print(Sca.getNumberofrecordes_censusdata(__correctFilepath))
    # print(Sca.getNumberofrecordes_statecode(__wrongFilepath))
    # print(Sca.iterator(__correctFilepath))
    ss = __StateSensusHandler(censusfilename=__correctFilepath,codefilename=__wrongFilepath)
    ss.Sorting_statesCensusDataOnArea()
    ss.Sorting_statesCensusDataOnopulationDensity()
