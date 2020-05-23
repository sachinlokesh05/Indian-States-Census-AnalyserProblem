'''

Custom Exception for census analyser

'''
class CensusException(Exception):
    pass

class FileNotCorrectException(CensusException):
    pass

class FileTypeNotCorrectException(CensusException):
    pass
class CsvFileHeaderException(CensusException):
    pass