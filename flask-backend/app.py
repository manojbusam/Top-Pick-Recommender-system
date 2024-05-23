from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dummy data for recommendations
recommendations_data = {
    "Manoj": [{"id": 101, "title": "Salaar"}, {"id": 102, "title": "Animal"}],
    "Vijju": [{"id": 103, "title": "Hi Nanna"}, {"id": 104, "title": "Nani's Majnu"}],
    "Kids": [{"id": 105, "title": "Shinchan"}, {"id": 106, "title": "Doremon"}]
}

@app.route('/api/recommend', methods=['GET'])
def recommend():
    user_id = f"{request.args.get('user_id')}"
    recommendations = recommendations_data.get(user_id, [])
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
