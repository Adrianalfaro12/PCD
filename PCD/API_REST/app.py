from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    return requests.get('https://catfact.ninja/fact').json()


if __name__ == "__main__":
    app.run(debug=True)