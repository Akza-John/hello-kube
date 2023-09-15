from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!!this is a updated statement"

if __name__ == '__main__':
    app.run(debug=True)

