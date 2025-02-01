import os
import pandas as pd
from abc import ABC,abstractmethod

# strategic pattern 
class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect(self, df:pd.DataFrame):
        pass


class SummaryInspectorStrategy(DataInspectionStrategy):
    
    def inspect(self, df:pd.DataFrame):
        print("\n summary statistics --- Numerical data")
        print(df.describe())
        print("\n summary statistics --- Categorical data")
        print(df.describe(include=["O"]))


class DataTypesInspectionStrategy(DataInspectionStrategy):

    def inspect(self, df:pd.DataFrame):
        print("\n analysing for the data type in the df")
        print(df.info())

        

class DataInspector:
    def __init__(self,strategy:DataInspectionStrategy):
        self._strategy = strategy

    def set_strategy(self,strategy:DataInspectionStrategy):
        self._strategy = strategy

    def execute_strategy(self, df:pd.DataFrame):
        self._strategy.inspect(df)


if __name__ == "__main__":
    df = pd.read_csv("")

    inspector = DataInspector(DataTypesInspectionStrategy())
    inspector.execute_strategy(df)

    inspector = DataInspector(SummaryInspectorStrategy())
    inspector.execute_strategy(df)








        
        