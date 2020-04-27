import pandas as pd
import os
class StateCensusAnalyser:
    
    def __init__(self, filename):
        target_path_1 = os.path.join(os.path.dirname(__file__), filename)
        datainput = pd.read_csv(target_path_1)
        #https://www.kaggle.com/danofer/india-census#india-districts-census-2011.csv
        print(datainput)


class CSVStateCensus:
    pass    

if __name__ == "__main__":
    Sca = StateCensusAnalyser(filename='indian_census_data_2011.csv')
    print(Sca)