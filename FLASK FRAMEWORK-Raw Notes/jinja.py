## How to Create an URL dynamically using Flask Request Module
### Jinja 2 TEmplate Engine
'''

'''
### Variables rule
from flask import Flask,render_template,request
'''
It Creates an instnce of the Flask Class
'''
app = Flask(__name__)


@app.route("/") # / Meams home page
def welcome():
    return "<html><H1>Welcome to HTML Flask Integration</H1></html>"

@app.route("/index",methods = ['GET'])
def sde():
    return render_template('index.html')

@app.route('/form',methods = ['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'   
    return render_template('form.html')

## Variable Rule 
@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL"
    return render_template('result.html',result = res)


if __name__ == "__main__":
    app.run(debug=True)