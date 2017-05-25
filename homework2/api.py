# написать GET ручку и разобраться и написать POST ручку

import requests
import flask
import json
from flask import Flask, jsonify, request
from flask import abort

app = flask.Flask(__name__)

users = [
    {'id': '0',
    'username': 'user1',
    'pass': '1234'},
    {'id': '1',
    'username': 'user2',
    'pass': '5678'}

    ]

@app.route('/')
def root():
    return 'Hello'

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify({'users': users})

@app.route('/api/user/<username>', methods=['GET'])
def show_user_profile(username):
    return 'Hello %s' % username

@app.route('/api/about', methods=['GET'])
def about():
    return 'The about page'

@app.route('/api/user', methods=['POST'])
def add_user():
    content = request.json
    users.append(content)
    print(content)
    return jsonify({'users' : users})

# для проверки POST:
# curl -X POST \
#   http://127.0.0.1:5000/user \
#   -H 'cache-control: no-cache' \
#   -H 'content-type: application/json' \
#   -H 'postman-token: a41b6b89-a76d-ee71-f683-6f7fdf57222c' \
#   -d '{
# "id": "2",
# "username": "user3",
# "pass": "9101"
# }'

if __name__ == '__main__':
    app.debug = True
    app.run()
