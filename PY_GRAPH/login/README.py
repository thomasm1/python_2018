from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "This Login made with Flask"
if __name__ == "__main__":
    app.run()
