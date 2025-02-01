import os 
import pandas as pd
from matplotlib import pyplot as plt
from abc import ABC ,abstractmethod
import seaborn as sns

class MissingValueAnalysisTemplate(ABC):
    def analysis(self,df:pd.DataFrame):
        self.identify_missing_values()
        self.visualize_missing_values()


    @abstractmethod
    def identify_missing_values(self,df:pd.DataFrame):
        pass
    
    def visualize_missing_values(self,df:pd.DataFrame):
        pass



class SimpleMissingValuesAnalysis(MissingValueAnalysisTemplate):
    def identify_missing_values(self, df:pd.DataFrame):
        print("\n Analysing the missing values in the given dataframe")
        missing_values = df.isnull().sum()
        print(missing_values[missing_values > 0])

    def visualize_missing_values(self, df:pd.DataFrame):
        plt.figure(figsize=(12,8))
        sns.heatmap(df.isnull(),cbar=False,cmap="viridis")
        plt.title("Mising values identification")
        plt.show()


if __name__ == "__main__":
    df = pd.read_csv("")
    missing_value_analyser = SimpleMissingValuesAnalysis()
    missing_value_analyser.analysis(df)
    missing_value_analyser.identify_missing_values(df)
    missing_value_analyser.visualize_missing_values(df)


  