from flask import Flask
from wsgiref import simple_server
import os

app = Flask(__name__)
@app.route ("/")
def main():
    return "hello"


port = int(os.getenv("PORT",5000))
if __name__ == "__main__":

    host = '0.0.0.0'
    #port = 5000
    httpd = simple_server.make_server(host, port, app)
    httpd.serve_forever()
