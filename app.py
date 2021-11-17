from flask import Flask, redirect, render_template, session, request, url_for
import socket
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/playvid', methods=['POST', 'GET'])
def handle_data():
    global FlaHost
    global FlaVid
    if request.method == 'POST':
       #result = request.form
       #return render_template("result.html",result = result)
       FlaHost = request.form['host']
       FlaVid = request.form['vid']
       r = requests.post('http://'+FlaHost+':8080/jsonrpc', json={"jsonrpc":"2.0","method":"Player.Open","params":{"item":{"file":FlaVid}},"id":1})
       #return render_template("result.html",result = result)
       #return render_template('index.html')
       return redirect(url_for('index'))


if __name__ == '__main__':
        app.run(host='0.0.0.0')