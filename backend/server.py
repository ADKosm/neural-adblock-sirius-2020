from flask import Flask, request
from flask_cors import CORS, cross_origin
import json


app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "Hello"


@app.route("/get")
@cross_origin()
def get():
    r = {
        "biba": request.args.get('v', "NONE")
    }
    return json.dumps(r)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
