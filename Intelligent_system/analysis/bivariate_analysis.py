import os
from abc import ABC,abstractmethod
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
class BivariateAnalysisStrategy(ABC):
    @abstractmethod
    def analyse(self,df:pd.DataFrame,feature:str):
        pass

class NumericalBivariateAnalysis(BivariateAnalysisStrategy):
    def analyse(self,df:pd.DataFrame,feature:str):
        print("Analysing numerical univariate analysis ")

        plt.figure(figsize=(10,6))
        sns.histplot(df[feature],kde=True,bins=30)

        plt.title(f"Distribution of features {feature}")
        plt.xlabel(feature)
        plt.ylabel("Frequency")
        plt.show()



class CategoricalBovariateAnalysis(BivariateAnalysisStrategy):
    def analyse(self,df:pd.DataFrame,feature:str):
        print("Categorical numerical univariate analysis ")

        plt.figure(figsize=(10,6))
        sns.histplot(df[feature],kde=True,bins=30)

        plt.title(f"Distribution of features {feature}")
        plt.xlabel(feature)
        plt.ylabel("Frequency")
        plt.show()






