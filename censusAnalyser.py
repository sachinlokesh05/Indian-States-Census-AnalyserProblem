import pandas as pd
import pathlib
from path import Path
import csv
import os
import json
from censusAnalyserException import *
from pandas.errors import ParserWarning,ParserError
from daoBaseClass import daoBaseClass

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
        global newDf # indian census and indian state code merged dataframe
        global __censusdataframe 
        __censusdataframe = StateCensusAnalyser.__init__(self,censusfilename)
        global  __statecodedataframe
        __statecodedataframe = StateCodeAnalyser.__init__(self,codefilename)

    '''
    Save the State Census Data into a Json File
    '''

    def to_stateCensusjsondata(self):
        
        sortedStatecesusData = self.__sort_statesDataInAlphabeticalOrdertojsonfile(data=__censusdataframe,column=['State'],to_filename=r'StateCensusJsondata.json')
        return sortedStatecesusData
    
    def to_stateCodejsondata(self):
        
        sortedStatecodeData = self.__sort_statesDataInAlphabeticalOrdertojsonfile(data=__statecodedataframe,column=['StateCode'],to_filename=r'StateCodeJsondata.json')
        return sortedStatecodeData

    def Sorting_statesCensusDataOnopulationDensity(self):
        return self.__sort_statesDataInAlphabeticalOrdertojsonfile(data=__censusdataframe,column=['DensityPerSqKm'],to_filename=r'StateCensusSortedonPopulationDensity.json')

    def Sorting_statesCensusDataOnArea(self):
        return self.__sort_statesDataInAlphabeticalOrdertojsonfile(data=__censusdataframe,column=['AreaInSqKm'],to_filename=r'StateCensusSortedonArea.json')

    def Check_statecoderecords(self,state=None):
        data = json.loads(self.Sorting_statesCodeDataInAlphabeticalOrder())
        State_list = list(data.get('StateCode').values())
        if state:
            return State_list.index(str(state))
        return State_list[0],State_list[len(State_list)-1] 

    def Check_statecensusurecords(self,state=None):
        data = json.loads(self.Sorting_statesCensusDataInAlphabeticalOrder())
        State_list = list(data.get('State').values())
        if state:
            return State_list.index(str(state))
        return State_list[0],State_list[len(State_list)-1]

    def check_recordsCountAfterSorted(self):
        return self.Sorting_statesCensusDataOnopulationDensity()
    
        
    '''

    Ability for Analyser to
    report the State Census
    Data in a Json Format
    according to State
    alphabetical order

    '''

    def Sorting_statesCensusDataInAlphabeticalOrder(self):
        # __censusdataframe = StateCensusAnalyser.__init__(self,__filename)
        return self.__sort_statesDataInAlphabeticalOrder(__censusdataframe,column='State').to_json()

    '''

    Ability for Analyser to
    report the State Census
    Data in a Json Format as
    per State Code in an
    alphabetical order

    '''

    def Sorting_statesCodeDataInAlphabeticalOrder(self):
        # __statecodedataframe = StateCodeAnalyser.__init__(self,__filename)
        return self.__sort_statesDataInAlphabeticalOrder(__statecodedataframe,column="StateCode").to_json()
    
    def __sort_statesDataInAlphabeticalOrder(self,data,column):
        '''

        With the python module inspect, one can inspect (not kidding) the run-time python stack. 
        Among other things, this makes it possible to get the name of the current function or callers. Handy for logging or debugging purposes. 

        '''
        try:
            column_data = daoBaseClass(column).getColumn()
            # if inspect.stack()[1][3]  == 'Sorting_statesCensusDataInAlphabeticalOrder' :
            return data.sort_values(by=column_data)
            # return "check the method again"

        except FileNotFoundError:
            FileNotCorrectException

        except FileExistsError :
            FileTypeNotCorrectException

    def __sort_statesDataInAlphabeticalOrdertojsonfile(self,data,column,to_filename):
        try:
            column_data = daoBaseClass(column).getColumn()
            data.sort_values(by=column_data,ascending=True).reset_index().to_json(to_filename,orient='records')
            return data.sort_values(by=column,ascending=True)
        except FileNotFoundError :
            raise FileNotCorrectException

        except FileExistsError :
            raise FileTypeNotCorrectException

        except CsvFileHeaderException :
            raise CsvFileHeaderException
    def mapping(self):
        # Read the files into two dataframes.
        df1 = __censusdataframe
        df2 = __statecodedataframe

        def __getDuplicateColumns(df):
            '''
            Get a list of duplicate columns.
            It will iterate over all the columns in dataframe and find the columns whose contents are duplicate.
            :param df: Dataframe object
            :return: List of columns whose contents are duplicates.
            '''
            duplicateColumnNames = set()
            # Iterate over all the columns in dataframe
            for x in range(df.shape[1]):
                # Select column at xth index.
                col = df.iloc[:, x]
                # Iterate over all the columns in DataFrame from (x+1)th index till end
                for y in range(x + 1, df.shape[1]):
                    # Select column at yth index.
                    otherCol = df.iloc[:, y]
                    # Check if two columns at x 7 y index are equal
                    if col.equals(otherCol):
                        duplicateColumnNames.add(df.columns.values[y])
            return list(duplicateColumnNames)

        def __get_duplicateColumnNames():
            print('Duplicate Columns are as follows')
            for col in duplicateColumnNames:
                print('Column name : ', col)

        df3 = pd.merge(df1,df2,left_on ="State",right_on="StateName")
        duplicateColumnNames = __getDuplicateColumns(df3)
        # __get_duplicateColumnNames()
        newDf = df3.drop(columns=__getDuplicateColumns(df3))
 
        newDf.to_csv('abc.csv',index=False)
        return newDf

if __name__ == "__main__" :

    # if input('do u want to specify file (y or n)').__contains__(['y','Y']):
    #     correctFilepath = input('enter file name: ')
    
    __correctFilepath = 'StateCensusData.csv'
    __wrongFilepath = 'StateCode.csv'
    Sca = _CSVStateCensus()
    print(__StateSensusHandler.mro())
    print(Sca.getNumberofrecordes_censusdata(__correctFilepath))
    print(Sca.getNumberofrecordes_statecode(__wrongFilepath))
    print(Sca.iterator(__correctFilepath))
    ss = __StateSensusHandler(censusfilename=__correctFilepath,codefilename=__wrongFilepath)
    print(ss.Sorting_statesCensusDataOnopulationDensity())
    print(ss.Sorting_statesCensusDataOnArea())

    print(ss.Check_statecensusurecords())
    print(ss.Check_statecoderecords())
    print(ss.check_recordsCountAfterSorted())
    print(ss.mapping())
    print(ss.to_stateCensusjsondata())
    print(ss.to_stateCodejsondata())
    print(ss.Sorting_statesCensusDataInAlphabeticalOrder())
    print(ss.Sorting_statesCodeDataInAlphabeticalOrder())