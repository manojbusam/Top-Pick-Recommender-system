from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dummy data for recommendations
recommendations_data = {
    1: [{"id": 101, "title": "Movie 1"}, {"id": 102, "title": "Movie 2"}],
    2: [{"id": 103, "title": "Movie 3"}, {"id": 104, "title": "Movie 4"}]
}

@app.route('/api/recommend', methods=['GET'])
def recommend():
    user_id = int(request.args.get('user_id'))
    recommendations = recommendations_data.get(user_id, [])
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
