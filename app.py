from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = 'My web application'
    return render_template("index.html", data=data)
