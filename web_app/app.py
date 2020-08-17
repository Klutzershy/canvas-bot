import json

from flask import Flask, request, render_template, Response
from flask_cors import CORS
from .cb_controller import register_user
from .cb_controller import login_user
from .cb_controller import update_preferences
#Initialize Flask App
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/register_user', methods=['POST'])
def register():
    post_data = request.get_json() #This gets the json object sent by the post request

    #print(post_data)
    if register_user(post_data):
        response = {"success": True}
        return Response(json.dumps(response), mimetype='application/json')
    else:
        response = {"success": False}
        return Response(json.dumps(response), mimetype='application/json')


@app.route('/login', methods=['POST'])
def login():
    post_data = request.get_json()

    #print(post_data)

    return login_user(post_data)

@app.route('/update_preferences', methods=['POST'])
def preferences():
    post_data = request.get_json()

    #print(post_data)

    return update_preferences(post_data)

app.run(debug=True)
