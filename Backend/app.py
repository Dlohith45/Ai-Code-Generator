from flask import Flask, request, jsonify
from flask_cors import CORS
from codes import PROGRAMS

app = Flask(__name__)
CORS(app)

@app.route('/generate', methods=['POST'])
def generate():

    data = request.get_json()

    prompt = data.get("prompt", "").lower()
    language = data.get("language", "Java")

    for keyword in PROGRAMS:
        if keyword.lower() in prompt.lower():
    

            code = PROGRAMS[keyword].get(
                language,
                "Language not supported"
            )

            return jsonify({"code": code})

    return jsonify({
        "code": "Program not found"
    })
if __name__ == '__main__':
    app.run(debug=True)