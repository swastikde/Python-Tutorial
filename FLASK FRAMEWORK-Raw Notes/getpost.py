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
    


if __name__ == "__main__":
    app.run(debug=True)