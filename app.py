from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Buzz12345',
    database='airportdb'
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/task/<task_name>')
def task(task_name):
    return render_template('task.html', task=task_name)

if __name__ == '__main__':
    app.run(debug=True)
