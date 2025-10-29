from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    try:
        connection = mysql.connector.connect(
            host="db",  # service name in docker-compose
            user="root",
            password="rootpassword",
            database="flaskdb"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT NOW();")
        result = cursor.fetchone()
        return jsonify({"message": "Connected to MySQL!", "time": str(result[0])})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
