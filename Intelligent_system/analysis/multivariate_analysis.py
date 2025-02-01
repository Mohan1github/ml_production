import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from abc import ABC,abstractmethod
import seaborn as sns



class MultivariateAnalysis(ABC):
    
    
    @abstractmethod
    def analyse_mutlivariate(self,df:pd.DataFrame):
        pass


class Num_Multivariate_Execution(MultivariateAnalysis):

    def analyse_mutlivariate(self, df:pd.Dataframe,feature:str):
    
        print("Analysing numerical multivariate analysis ")

        plt.figure(figsize=(10,6))
        sns.histplot(df[feature],kde=True,bins=30)

        plt.title(f"Distribution of features {feature}")
        plt.xlabel(feature)
        plt.ylabel("Frequency")
        plt.show()


class Cat_Multivariate_Execution(MultivariateAnalysis):

    def analyse_mutlivariate(self, df:pd.Dataframe,feature:str):

        print("Analysing Categorical multivariate analysis ")

        plt.figure(figsize=(10,6))
        sns.histplot(df[feature],kde=True,bins=30)

        plt.title(f"Distribution of features {feature}")
        plt.xlabel(feature)
        plt.ylabel("Frequency")
        plt.show()


        

if __name__ == "__main__":



        