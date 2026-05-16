from flask import Flask, request, jsonify
from logic import calculate
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "Calculator App Running"


@app.route("/api/calculate", methods=["GET"])
def calc():

    expression = request.args.get("expr")

    if not expression:
        return jsonify({"error": "No expression provided"}), 400

    try:

        result = calculate(expression)

        return jsonify({
            "expression": expression,
            "result": result
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
