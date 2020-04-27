import pytest
from censusAnalyser import CSVStateCensus as csvdata
from censusAnalyserException import *

'''

Given the States Census CSV file, Check to ensure the Number of Record matches

'''

def test_Happy_Test_Case_where_the_records_are_checked_TC_1_1():
    correctFilepath = 'StateCensusData.csv'
    wrongFilepath = 'StateCensusData1.csv'
    assert csvdata(correctFilepath).getNumberofrecordes() == 29

# @pytest.mark.xfail(raises=CensusException)
def test_Given_the_State_Census_CSV_File_if_incorrect_Returns_a_custom_Exception_TC_1_2():
    correctFilepath = 'StateCensusData.csv'
    wrongFilepath = 'StateCensusData1.csv'

    with pytest.raises(CensusException):
            csvdata(wrongFilepath).getNumberofrecordes()

if __name__ == "__main__":
    pytest.main()