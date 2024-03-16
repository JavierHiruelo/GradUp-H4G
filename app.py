# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify, json


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cv')
def cv():
    return render_template('cv.html')


@app.route('/search')
def search():
    return render_template('search.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

