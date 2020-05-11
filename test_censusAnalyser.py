import pytest
from censusAnalyser import _CSVStateCensus as csvdata,__StateSensusHandler as handler
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

@pytest.mark.xfail(raises=FileTypeNotCorrectException)
def test_Given_the_State_Census_CSV_File_when_correct_but_type_incorrect_Returns_a_custom_Exception_TC_2_3():
    wrongFiletype = 'StateCode.txt'

    # with pytest.raises(FileNotFoundError):
    csvdata().getNumberofrecordes_statecode(wrongFiletype)
    

'''

For Test Case to pass check the start and end states of State CensusData in a Json Format asper State Census in an alphabetical order

'''
def test_to_pass_check_the_start_and_end_statestion_TC_3_1():
    censusfile = 'StateCensusData.csv'
    codefile = 'StateCode.csv'
    starting_state,ending_state = handler(censusfile,codefile).Check_statecensusurecords()

    assert starting_state == 'Andhra Pradesh' and ending_state == 'West Bengal'


'''

For Test Case to pass check the particular state of State CensusData in a Json Format asper State Census in an alphabetical order

'''
def test_to_pass_check_the_particular_state_TC_3_2():
    censusfile = 'StateCensusData.csv'
    codefile = 'StateCode.csv'
    state = 'Kerala'
    starting_state = handler(censusfile,codefile).Check_statecensusurecords(state=state)

    assert starting_state == 12


'''

For Test Case to pass check the start and end states of State Code Data in a Json Format asper State Code in an alphabetical order

'''
def test_to_pass_check_the_start_and_end_statestion_TC_4_1():
    censusfile = 'StateCensusData.csv'
    codefile = 'StateCode.csv'
    starting_state,ending_state = handler(censusfile,codefile).Check_statecoderecords()

    assert starting_state == 'AD' and ending_state == 'WB'


'''

For Test Case to pass check the particular state of State Code Data in a Json Format asper State Code in an alphabetical order

'''
def test_to_pass_check_the_particular_state_TC_4_2():
    censusfile = 'StateCensusData.csv'
    codefile = 'StateCode.csv'
    state = 'KA'
    starting_state = handler(censusfile,codefile).Check_statecoderecords(state=state)

    assert starting_state == 17


'''

For Test Case to pass report Number of States Count Before Sorting and Number of States Count After Sorting

'''
def test_For_Test_Case_to_pass_report_number_of_states_sorted_TC_5_1():
    censusfile = 'StateCensusData.csv'
    codefile = 'StateCode.csv'
    
    ''' Number of States Count Before Sorting'''
    numberOfStatesBeforeSorting = csvdata().getNumberofrecordes_censusdata(censusfile)

    ''' Number of States Count After Sorting''' 
    numberOfStatesAfterSorting = handler(censusfile,codefile).check_recordsCountAfterSorted()

    
    assert numberOfStatesAfterSorting == numberOfStatesBeforeSorting



if __name__ == "__main__":
    pytest.main()