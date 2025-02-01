import os
from abc import ABC,abstractmethod
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

import seaborn as sns


class UnivariateAnalysisStrategy(ABC):
    @abstractmethod
    def analyse(self,df:pd.DataFrame,feature:str):
        pass

class NumericalUnivariateAnalysis(UnivariateAnalysisStrategy):
    def analyse(self,df:pd.DataFrame,feature:str):

        print("Analysing numerical univariate analysis ")

        plt.figure(figsize=(10,6))
        sns.histplot(df[feature],kde=True,bins=30)

        plt.title(f"Distribution of features {feature}")
        plt.xlabel(feature)
        plt.ylabel("Frequency")
        plt.show()


class CategoricalUnivariateAnalysis(UnivariateAnalysisStrategy):
    def analys(self,df:pd.DataFrame,feature:str):
        print("Analysing Categorical  univariate analysis ")

        plt.figure(figsize=(10,6))
        sns.histplot(df[feature],kde=True,bins=30)

        plt.title(f"Distribution of features {feature}")
        plt.xlabel(feature)
        plt.ylabel("Frequency")
        plt.show()


if __name__ == "__main__":
    df = pd.read_csv("")
    feature = ""
    num_univariate_analyser = NumericalUnivariateAnalysis()
    num_univariate_analyser.analyse(df,feature)

    cat_univariate_analyser = CategoricalUnivariateAnalysis()
    cat_univariate_analyser.analyse(df,feature)




