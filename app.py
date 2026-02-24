from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return {"status": "Branched Changed Successfully After Merge"}

@app.route("/infer", methods=["POST"])
def infer():
    data = request.get_json(force=True)

    # Dummy inference logic (replace later)
    text = data.get("text", "")
    result = text.upper()

    return jsonify({
        "input": text,
        "output": result
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

