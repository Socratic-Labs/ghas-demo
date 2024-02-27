from flask import Flask, request
import requests

test_webhook_app = Flask(__name__)

@test_webhook_app.route('/greeting')
def greeting():
    return 'Hello, World!'

@test_webhook_app.route("/user_picture1")
# from: https://codeql.github.com/codeql-query-help/python/py-path-injection/#example
def user_picture1():
    filename = request.args.get('p')
    # BAD: This could read any file on the file system
    data = open(filename, 'rb').read()
    return data

@test_webhook_app.route('/')
def home():
    return 'vulnerable home route'
    # return '''<h1>SSRF</h1>
    #             <br>
    #             Usage:
    #                 <br><code>http://127.0.0.1:80/follow?url=https://api.github.com/events</code><br>
    #             Running:
    #             <br><code>
    #                 sudo apt install -y python3-pip
    #                 sudo pip3 install flask requests;
    #                 FLASK_APP=ssrf.py flask run --host=0.0.0.0 --port=80
    #             </code></br>
    # '''


if __name__ == '__main__':

    test_webhook_app.run( debug=True )