from flask import Flask, request, jsonify
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
    if user_id:
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
            cur.execute("SELECT relevancy, title FROM toppicks_recommendations WHERE user_id = %s ORDER BY relevancy DESC", (user_id,))
            results = cur.fetchall()

            # Format results
            recommendations = [{'relevancy': row[0], 'title': row[1]} for row in results]

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    return jsonify(recommendations)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5000)
