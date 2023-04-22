from flask import Flask, request, jsonify
import os
import openai
from flask_cors import CORS
#from dotenv import load_dotenv

#load_dotenv()
openai.api_key = os.getenv("OPEN_API_KEY")

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['POST'])
def resul():
    prompt = request.json['prompt']
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

