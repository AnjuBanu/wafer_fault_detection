from wsgiref import simple_server
from flask import Flask, render_template, request, Response
from flask_cors import CORS, cross_origin
from prediction_Validation_Insertion import pred_validation
from logger import App_Logger

app=Flask(__name__)
app.debug = True
CORS(app)

@app.route("/", methods = ['GET'])
@cross_origin()
def home():
    file = open("Logs/prediction_log.txt", "a+")
    log_writer = App_Logger()
    log_writer.log(file, "Start")
    return render_template("index.html")



@app.route("/predict", methods = ['POST'])
@cross_origin()
def predict_data():
    try:
        if request.json is not None:
            path = request.json ['filepath']
            print(path)
            pred_val = pred_validation(path)
            pred_val.prediction_validation()
        elif request.form is not None:
            path = request.form ['filepath']
            print(path)
            pred_val = pred_validation(path)
            pred_val.prediction_validation()


    except ValueError:
        return Response("Error Occurred! %s" % ValueError)
    return ""

def train_data():
    train_val = pred_validation("Training_Batch_Files")
    train_val.prediction_validation()


if __name__ == "__main__":
    train_data()
    url="localhost"
    host=8080
    httpd = simple_server.make_server(url,host,app)
    httpd.serve_forever()