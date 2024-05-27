from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Define database connection parameters
db_params = {
    'dbname': "recommendations_db",
    'user': "user",
    'password': "password",
    'host': "127.0.0.1",
    'port': "5432"
}

# Route to recommend endpoint
@app.route('/api/recommend', methods=['GET'])
def recommend():
    user_id = request.args.get('user_id')
    recommendations = []
    conn = None
    try:
        # Connect to the database
        conn = psycopg2.connect(
            dbname=db_params['dbname'],
            user=db_params['user'],
            password=db_params['password'],
            host=db_params['host'],
            port=db_params['port']
        )
        cur = conn.cursor()

        # Execute SQL query
        cur.execute("SELECT title FROM toppicks_recommendations WHERE user_id = %s ", (user_id,))
        results = cur.fetchall()

        # Format results
        recommendations = [row[0] for row in results]

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return jsonify({'error': 'An error occurred while fetching recommendations.'}), 500
    finally:
        if conn is not None:
            conn.close()

    return jsonify(recommendations)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5000)

