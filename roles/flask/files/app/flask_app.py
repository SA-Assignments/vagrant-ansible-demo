#!/usr/bin/env python

from flask import Flask, request, render_template
import pymysql

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

db = pymysql.connect("10.0.0.10", "root", "hello", "webapp")



@app.route('/db')
def someName():
    cursor = db.cursor()
    sql = "SELECT * FROM pet"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('index.html', results=results)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
