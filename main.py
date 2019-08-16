from flask import Flask
from datetime import datetime
import time
from flask import Flask, render_template, request, redirect
import requests


now = datetime.now() # current date and time
date = now.strftime("%d %b, %Y")

app = Flask(__name__, template_folder='C:/Users/ddm50/.PyCharm2019.2/config/scratches')

username = "ddm50"

@app.route('/')
def user():
    ip = requests.get("http://ip-api.com/json/")
    location = ip.json()
    country = location["country"]
    return f'User: ({username})<br><br> Location: {country}<br><br>Welcome {username}, today is {date}<br><br> <a href="/login"> Login </a>'

@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            return render_template("failed.html")
        else:
            redirect("/")
    return render_template('login.html', error=error)

@app.errorhandler(404)
def page_not_found(error):
    return '<h1 color="red"> 404 Page Not Found </h1>', 404

if __name__ =="__main__":
    app.run(debug=True,port=8080)
