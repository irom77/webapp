from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/hello/<name>')
def hello(name):
    r = requests.get('www.google.com')
    #return render_template('page.html', name=name)    
    return r.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0')
