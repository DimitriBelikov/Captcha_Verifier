from flask import Flask, render_template, request, redirect, url_for
from captcha import Captcha
from os import listdir

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET','POST'])
def homepage():
    if request.method == 'GET':
        captcha = Captcha().create_captcha()
        return render_template('homepage.html', captcha=captcha)

@app.route('/check', methods=['POST'])
def check():
    if request.method == 'POST':
        user_text = request.form['user_text']
        if user_text+'.jpeg' in listdir('./static') :
            Captcha.delete_captcha(user_text+'.jpeg')
            return redirect(url_for('success'))
        else:
            return '<h1> Login UnSuccessfull !!! <h1>'

@app.route('/success')
def success():
   return '<h1> Login Successfull !!! <h1>'