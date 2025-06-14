from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/test")
def test():
    return jsonify({"status": "success"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
