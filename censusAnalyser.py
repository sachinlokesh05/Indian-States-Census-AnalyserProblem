import pandas as pd
import os
class StateCensusAnalyser:
    
    def __init__(self, filename):
        target_path_1 = os.path.join(os.path.dirname(__file__), filename)
        self.csv_data = pd.read_csv(target_path_1)


class CSVStateCensus(StateCensusAnalyser):
    
    def __init__(self, filename):
        super().__init__(filename)   

if __name__ == "__main__":
    Sca = CSVStateCensus(filename='indian_census_data_2011.csv')
    print(Sca.csv_data)