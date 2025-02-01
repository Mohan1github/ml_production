import os
import zipfile
from abc import ABC, abstractmethod
import pandas as pd

# factory design pattern 
class DataIngestor(ABC):
    @abstractmethod
    def ingest(self,file_path:str) -> pd.DataFrame:
       pass



# class for doing the main converions by abstracting the DataIngestor
class ZipDataIngestor(DataIngestor):

    def ingest(self,file_path:str) -> pd.DataFrame:

        if not file_path.endswith(".zip"):
            raise ValueError("The provided file is not .zip file format")
        
        with zipfile.ZipFile(file_path,'r') as zip_file:
            zip_file.extractall("extracted_data")

        extracted_files = os.listdir("extracted_file")
        csv_files = [k for k in extracted_files if k.endswith(".csv")]

        if(len(csv_files) == 0):
            raise ValueError("No csv file found in the given zipped file")
        if(len(csv_files) > 1):
            raise ValueError("More than  csv file is ")

        csv_file_path = os.path.join("extracted_data",csv_files[0])

        df = pd.read_csv(csv_file_path)


        return df
    
class DataIngestorFactory:
    @staticmethod
    def get_data_ingestor(file_extension: str) -> DataIngestor:
        if file_extension == ".zip":
            return ZipDataIngestor()
        else:
            raise ValueError(f"No data ingestor available for the extensio {file_extension}")
        
if __name__ == "__main__":
    file_path = ""

    file_extention = os.path.splitext()[1]

    data_ingestor = DataIngestorFactory.get_data_ingestor(file_extension = file_extention)

    df = data_ingestor.ingest(file_path)

    print(df.head())

    






