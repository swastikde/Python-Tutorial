from flask import Flask 
'''
It Creates an instnce of the Flask Class
'''
app = Flask(__name__)


@app.route("/") # / Meams home page
def welcome():
    return "Welcome to Flask Tutorial."

@app.route("/sde")
def sde():
    return "This is the welcome page for Swastik."

if __name__ == "__main__":
    app.run(debug=True)