import json
from logger import App_Logger
from flask import Response


class Predicted_data_validation:
    def __init__(self, path):
        self.path = path
        self.schema_path = 'schema_prediction.json'
        self.log_writer = App_Logger()

    def validateSchema(self):
        try:
            with open(self.schema_path, 'r') as f:
                print("before")
                data_info = json.load(f)
                print(data_info)
                f.close()
            name_pattern = data_info["SampleFileName"]
            LengthOfDateStampInFile = data_info["LengthOfDateStampInFile"]
            LengthOfTimeStampInFile = data_info['LengthOfTimeStampInFile']
            NumberofColumns = data_info['NumberofColumns']
            ColName = data_info['ColName']

            file=open("Logs/prediction_log.txt","a+")
            self.log_writer.log(file,f"File name pattern::{name_pattern}"
                                         f"||Date length::{LengthOfDateStampInFile}"
                                         f"||Time length::{LengthOfTimeStampInFile}"
                                    )
        except ValueError:
            return Response("Error Occurred! %s" % ValueError)


