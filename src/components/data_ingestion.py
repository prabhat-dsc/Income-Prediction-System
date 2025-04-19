import os,sys
from src.exception import CustmeException
from src.logger import logging
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split


@dataclass
class DataIngestionConfig:
    raw_data_path=os.path.join("artifacts","raw.csv")
    train_data_path=os.path.join("artifacts","train.csv")
    test_data_path=os.path.join("artifacts","test.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig() 

    def inititate_data_ingestion(self):
        logging.info("Data Ingestion Started")
        try:
            logging.info("Getting raw data from source")
            data=pd.read_csv('raw.csv')
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=True,header=True) 
            logging.info(" Raw data ingestion completed")
            logging.info(" Data splition for train and test set started") 
            train_set,test_set= train_test_split(data,test_size=0.3,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path)
            test_set.to_csv(self.ingestion_config.test_data_path)
            logging.info(" Data Ingestion  completed")
            logging.info(" Returning train and test set path")
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.info(" Error occured in Data Ingestion")
            raise CustmeException (e,sys)
        

"""
if __name__=="__main__":
    obj=DataIngestion()
    obj.inititate_data_ingestion()
"""
