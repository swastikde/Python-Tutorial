from flask import Flask, render_template
'''
It Creates an instnce of the Flask Class
'''
app = Flask(__name__)


@app.route("/") # / Meams home page
def welcome():
    return "<html><H1>Welcome to HTML Flask Integration</H1></html>"

@app.route("/sde")
def sde():
    return render_template('index.html')

@app.route('/about')
def about():
    

if __name__ == "__main__":
    app.run(debug=True)