from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname="recommendations_db",
    user="user",
    password="password",
    host="127.0.0.1",  # or your database host
    port="5432"  # default PostgreSQL port
)

@app.route('/api/recommend', methods=['GET'])
def recommend():
    user_id = request.args.get('user_id')
    recommendations = []
    if user_id:
        cursor = conn.cursor()
        cursor.execute("SELECT movie_id, title FROM recommendations WHERE user_id=%s", (user_id,))
        recommendations = [{'id': row[0], 'title': row[1]} for row in cursor.fetchall()]
        cursor.close()
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
