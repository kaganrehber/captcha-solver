from flask import Flask, request, jsonify
from app import solve_captcha

app = Flask(__name__)

@app.route("/solve", methods=["POST"])
def solve():
    data = request.get_json()

    if not data or "image" not in data:
        return jsonify({"error": "Missing 'image' field"}), 400

    try:
        result = solve_captcha(data["image"])
        return jsonify({"text": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
