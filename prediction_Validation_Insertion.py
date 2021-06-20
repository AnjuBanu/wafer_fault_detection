from logger import App_Logger
from flask import Response
from predicted_data_validation import Predicted_data_validation

class pred_validation:
    def __init__(self, path):
        self.raw_data = Predicted_data_validation(path)
        self.log_writer = App_Logger()
        self.file = open("Logs/prediction_log.txt","a+")

    def prediction_validation(self):
        try:
            name_pattern, LengthOfDateStampInFile, LengthOfTimeStampInFile, NumberofColumns, ColName =self.raw_data.validateSchema()
            self.raw_data.validateNamePattern(name_pattern,LengthOfDateStampInFile,LengthOfTimeStampInFile)
            self.raw_data.validateNumberofColumns(NumberofColumns)
            self.raw_data.validateColName(ColName)


        except ValueError:
            return Response("Error Occurred! %s" % ValueError)
        return True
