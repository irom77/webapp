from flask import Flask, jsonify
import os, requests, sys, socket

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(
        host=socket.gethostname()
    )

@app.route('/backend')
def backend():    
    r = requests.get(os.environ['URL'])
    return r.json()['host']

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0',port=int(sys.argv[1]))
