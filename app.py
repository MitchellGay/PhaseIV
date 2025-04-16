from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL Connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Buzz12345',
    database='airportdb'
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json.get('message')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (text) VALUES (%s)", (data,))
    conn.commit()
    cursor.close()
    return jsonify({'status': 'success', 'message': data})

if __name__ == '__main__':
    app.run(debug=True)
