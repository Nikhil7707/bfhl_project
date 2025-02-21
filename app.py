from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def process_data():
    data = request.json.get("data", [])
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    highest_alphabet = [max(alphabets, key=str.lower)] if alphabets else []

    response = {
        "is_success": True,
        "user_id": "john_doe_17091999",
        "email": "john@xyz.com",
        "roll_number": "ABCD123",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": highest_alphabet
    }
    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def get_code():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)
