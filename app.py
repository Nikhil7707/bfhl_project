from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/bfhl', methods=['POST'])
def process_data():
    data = request.json.get("data", [])
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    highest_alphabet = [max(alphabets, key=str.lower)] if alphabets else []

    response = {
        "is_success": True,
        "user_id": "your_name_ddmmyyyy",
        "email": "your_college_email",
        "roll_number": "your_roll_number",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": highest_alphabet
    }
    return jsonify(response), 200

@app.route('/bfhl', methods=['GET'])
def get_code():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000, debug=True)
