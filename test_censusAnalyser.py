import pytest
from censusAnalyser import CSVStateCensus as csvdata
from censusAnalyserException import *

'''

Given the States Census CSV file, Check to ensure the Number of Record matches

'''

def test_Happy_Test_Case_where_the_records_are_checked_TC_1_1():
    correctFilepath = 'StateCensusData.csv'
    wrongFilepath = 'StateCensusData1.csv'
    assert csvdata().getNumberofrecordes_censusdata(correctFilepath) == 29

'''

Given the State Census CSV File if incorrect Returns a custom Exception

'''

@pytest.mark.xfail(raises=FileNotCorrectException)
def test_Given_the_State_Census_CSV_File_if_incorrect_Returns_a_custom_Exception_TC_1_2():
    wrongFilepath = 'StateCensusData.csv'

    # with pytest.raises(FileNotCorrectException):
    csvdata().getNumberofrecordes_censusdata(wrongFilepath)
            
'''

Given the State Census CSV File when correct but type incorrect Returns a custom Exception

'''
@pytest.mark.xfail(raises=FileTypeNotCorrectException)
def test_Given_the_State_Census_CSV_File_when_correct_but_type_incorrect_Returns_a_custom_Exception_TC_1_3():
    wrongFiletype = 'StateCensusData.txt'

    # with pytest.raises(FileNotFoundError):
    csvdata().getNumberofrecordes_censusdata(wrongFiletype)

'''

Given the States code CSV file, Check to ensure the Number of Record matches

'''

def test_Happy_Test_Case_where_the_records_are_checked_TC_2_1():
    correctFilepath = 'StateCode.csv'
    wrongFilepath = 'StateCensusData1.csv'
    assert csvdata().getNumberofrecordes_statecode(correctFilepath) == 37

'''

Given the State Code CSV File if incorrect Returns a custom Exception

'''

@pytest.mark.xfail(raises=FileNotCorrectException)
def test_Given_the_State_Code_CSV_File_if_incorrect_Returns_a_custom_Exception_TC_2_2():
    wrongFilepath = 'StateCode.csv'

    # with pytest.raises(FileNotCorrectException):
    csvdata().getNumberofrecordes_statecode(wrongFilepath)
            
'''

Given the State Code CSV File when correct but type incorrect Returns a custom Exception

'''
@pytest.mark.xfail(raises=FileTypeNotCorrectException)
def test_Given_the_State_Census_CSV_File_when_correct_but_type_incorrect_Returns_a_custom_Exception_TC_2_3():
    wrongFiletype = 'StateCode.txt'

    # with pytest.raises(FileNotFoundError):
    csvdata().getNumberofrecordes_statecode(wrongFiletype)

if __name__ == "__main__":
    pytest.main()