import pytest
from censusAnalyser import CSVStateCensus as csvdata

'''

Given the States Census CSV file, Check to ensure the Number of Record matches

'''

def test_Happy_Test_Case_where_the_records_are_checked_TC_1_1():
    correctFilepath = 'StateCensusData.csv'
    wrongFilepath = 'StateCensusData1.csv'
    assert csvdata(correctFilepath).getNumberofrecordes() == 29

if __name__ == "__main__":
    pytest.main()