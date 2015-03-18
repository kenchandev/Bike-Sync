import json
import os
from flask import Flask, render_template, request, redirect, jsonify
from bson import json_util
from pymongo import MongoClient

def connect():
# Substitute the 5 pieces of information you got when creating
# the Mongo DB Database (underlined in red in the screenshots)
# Obviously, do not store your password as plaintext in practice
    connection = MongoClient("ds062097.mongolab.com",62097)
    handle = connection["citibike"]
    handle.authenticate("root","root")
    return handle

app = Flask(__name__)
handle = connect()

def retrieve_data(quantity, data_year):
    options = {
        "12-2014": list(handle._2014_12.find().limit(int(quantity))),
        "11-2014": list(handle._2014_11.find().limit(int(quantity))),
        "10-2014": list(handle._2014_10.find().limit(int(quantity))),
        "09-2014": list(handle._2014_09.find().limit(int(quantity))),
        "08-2014": list(handle._2014_08.find().limit(int(quantity))),
        "07-2014": list(handle._2014_07.find().limit(int(quantity))),
        "06-2014": list(handle._2014_06.find().limit(int(quantity))),
        "05-2014": list(handle._2014_05.find().limit(int(quantity))),
        "04-2014": list(handle._2014_04.find().limit(int(quantity))),
        "03-2014": list(handle._2014_03.find().limit(int(quantity))),
        "02-2014": list(handle._2014_02.find().limit(int(quantity))),
        "01-2014": list(handle._2014_01.find().limit(int(quantity))),
        "12-2013": list(handle._2013_12.find().limit(int(quantity))),
        "11-2013": list(handle._2013_11.find().limit(int(quantity))),
        "10-2013": list(handle._2013_10.find().limit(int(quantity))),
        "09-2013": list(handle._2013_09.find().limit(int(quantity))),
        "08-2013": list(handle._2013_08.find().limit(int(quantity)))
    }
    return options[data_year]

# Bind our index page to both www.domain.com/ and www.domain.com/index
@app.route("/index" ,methods=['GET'])
@app.route("/", methods=['GET'])
def index():
    # userinputs = [x for x in handle._2014_10.find()]
    # return render_template('index.html', userinputs=userinputs)
    return render_template('index.html')

@app.route("/write", methods=['POST'])
def write():
    userinput = request.form.get("userinput")
    oid = handle._2014_10.insert({"message":userinput})
    return redirect ("/")

@app.route("/deleteall", methods=['GET'])
def deleteall():
    handle._2014_10.remove()
    return redirect ("/")

@app.route("/api/12-2014/<quantity>", methods=['GET'])
def get_12_2014(quantity):
    return json.dumps(retrieve_data(quantity, "12-2014"), default=json_util.default)

@app.route("/api/11-2014/<quantity>", methods=['GET'])
def get_11_2014(quantity):
    return json.dumps(retrieve_data(quantity, "11-2014"), default=json_util.default)

@app.route("/api/10-2014/<quantity>", methods=['GET'])
def get_10_2014(quantity):
    return json.dumps(retrieve_data(quantity, "10-2014"), default=json_util.default)

@app.route("/api/09-2014/<quantity>", methods=['GET'])
def get_09_2014(quantity):
    return json.dumps(retrieve_data(quantity, "09-2014"), default=json_util.default)

@app.route("/api/08-2014/<quantity>", methods=['GET'])
def get_08_2014(quantity):
    return json.dumps(retrieve_data(quantity, "08-2014"), default=json_util.default)

@app.route("/api/07-2014/<quantity>", methods=['GET'])
def get_07_2014(quantity):
    return json.dumps(retrieve_data(quantity, "07-2014"), default=json_util.default)

@app.route("/api/06-2014/<quantity>", methods=['GET'])
def get_06_2014(quantity):
    return json.dumps(retrieve_data(quantity, "06-2014"), default=json_util.default)

@app.route("/api/05-2014/<quantity>", methods=['GET'])
def get_05_2014(quantity):
    return json.dumps(retrieve_data(quantity, "05-2014"), default=json_util.default)

@app.route("/api/04-2014/<quantity>", methods=['GET'])
def get_04_2014(quantity):
    return json.dumps(retrieve_data(quantity, "04-2014"), default=json_util.default)

@app.route("/api/03-2014/<quantity>", methods=['GET'])
def get_03_2014(quantity):
    return json.dumps(retrieve_data(quantity, "03-2014"), default=json_util.default)

@app.route("/api/02-2014/<quantity>", methods=['GET'])
def get_02_2014(quantity):
    return json.dumps(retrieve_data(quantity, "02-2014"), default=json_util.default)

@app.route("/api/01-2014/<quantity>", methods=['GET'])
def get_01_2014(quantity):
    return json.dumps(retrieve_data(quantity, "01-2014"), default=json_util.default)

@app.route("/api/12-2013/<quantity>", methods=['GET'])
def get_12_2013(quantity):
    return json.dumps(retrieve_data(quantity, "12-2013"), default=json_util.default)

@app.route("/api/11-2013/<quantity>", methods=['GET'])
def get_11_2013(quantity):
    return json.dumps(retrieve_data(quantity, "11-2013"), default=json_util.default)

@app.route("/api/10-2013/<quantity>", methods=['GET'])
def get_10_2013(quantity):
    return json.dumps(retrieve_data(quantity, "10-2013"), default=json_util.default)

@app.route("/api/09-2013/<quantity>", methods=['GET'])
def get_09_2013(quantity):
    return json.dumps(retrieve_data(quantity, "09-2013"), default=json_util.default)

@app.route("/api/08-2013/<quantity>", methods=['GET'])
def get_08_2013(quantity):
    return json.dumps(retrieve_data(quantity, "08-2013"), default=json_util.default)

# Remove the "debug=True" for production
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))

    app.run(host='0.0.0.0', port=port, debug=True)