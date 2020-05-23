import re
from censusAnalyserException import CsvFileHeaderException

class daoBaseClass(object):
    
    def __init__(self,columnList):
        
        if re.search(r'(StateName|StatesName|State|StateNames|StateNames)',str(columnList)): self.State = columnList

        elif re.search(r'(StateCode|StatesCode|StateCodes|StatesCodes)',str(columnList)): self.StateCode = columnList  

        elif re.search(r'(DensityPerSqKm|Density)',str(columnList)): self.DensityPerSqKm = columnList

        elif re.search(r'(AreaInSqKm|Area)',str(columnList)): self.area = columnList

        else :raise CsvFileHeaderException()

    def getColumn(self):
        
        if 'State' in dir(self) :
            return self.State
        elif 'StateCode' in dir(self) :
            return self.StateCode
        elif 'population' in dir(self):
            return self.population 
        elif 'DensityPerSqKm' in dir(self):
            return self.DensityPerSqKm 
        elif 'DensityPerSqKm' in dir(self):
            return self.DensityPerSqKm
        elif 'area' in dir(self):
            return self.area
        else:
            return None

if __name__ == "__main__" :
    pass