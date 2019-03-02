from flask import Flask
from flask import request
from flask import jsonify
from flask import send_file

import simplejson

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    #serve the index.html
    return send_file('index.html');

@app.route('/', methods=['POST'])
def respond():
    #load the request
    dict = simplejson.loads(request.data)

    #read the string sent from the frontend
    composerName = dict['composerName']

    #calculations/processing..

    result = {}
    #load data into a dictionary like so
    result['composer'] = composerName
    result['testdata1'] = 'test1'
    result['testdata2'] = 'test2'

    #return the data to the frontend
    response = jsonify(result)
    return response

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)
