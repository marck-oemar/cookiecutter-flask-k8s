from flask import Flask
from flask import request
from os import environ
import json
'''
description: 
'''

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home(): 
    return "<h1>Hello world</h1><p>This is a preview page for our project {{cookiecutter.project_name}}.</p>"

@app.route('/api/postme', methods=['POST'])
def postme():
    try:
        try:
            body = request.json
        except:
            return "body is not correct or available:", 400
        return "Thanks you!", 201
    except:
        return "", 500

@app.route('/api/getme', methods=['GET'])
def getme():
    try:
        return "What do you mean, get me?", 201
    except:
        return "", 500

# Run the service on the local server it has been deployed to,
# listening on port 8080.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)