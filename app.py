import json

from flask import Flask, render_template, request
import contraller

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    name = request.form.get("name")
    pwd = request.form.get("pwd")
    res = contraller.login(name, pwd)
    return json.dumps({"result": res})


@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    pwd = request.form.get('pwd')
    email = request.form.get('email')
    res = contraller.register(name, pwd, email)
    return json.dumps({"result": res})


if __name__ == '__main__':
    app.run()
