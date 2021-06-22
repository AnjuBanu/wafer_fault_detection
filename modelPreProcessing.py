
from logger import App_Logger
import pandas as pd

class Model_Preprocessing:
    def __init__(self,perform):
        self.log_writer = App_Logger()
        self.task=perform
        self.final_csv = "Final_csv/"
        if self.task == "train":
            self.log_file = "Logs/train_log.txt"
        else:
            self.log_file = "Logs/prediction_log.txt"

    def trainModel(self):
        file_log = open(self.log_file, "a+")
        self.log_writer.log(file_log, "Training Started !!")
        wafer_data = pd.read_csv(self.final_csv+"train_Input.csv")
        pass