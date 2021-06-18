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
            self.log_writer.log(self.file, "Start of Validation of file:!")
            self.raw_data.validateSchema()

        except ValueError:
            return Response("Error Occurred! %s" % ValueError)
        return True
