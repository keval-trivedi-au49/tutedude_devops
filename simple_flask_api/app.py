from flask import Flask, jsonify
import json
app = Flask(__name__)

@app.route("/api")
def get_data():
    try:
        with open("jsonData.json", "r") as file:
            data = json.load(file)
        return jsonify(data), 200
    except FileNotFoundError:
        return jsonify({
            "error": "JSON file not found"
        }), 404

    except json.JSONDecodeError:
        return jsonify({
            "error": "Invalid JSON data in file"
        }), 500

    except Exception as error:
        return jsonify({
            "error": str(error)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)