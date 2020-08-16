import json

from flask import Flask, request, render_template, Response
from flask_cors import CORS
#import cb_controller
#from CBController import cb_controller

#Initialize Flask App
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/register_user', methods=['POST'])
def register():
    post_data = request.get_json() #This gets the json object sent by the post request

    print(post_data)

    response = {"success": True}
    return Response(json.dumps(response), mimetype='application/json')

#app.register_blueprint(cb_controller, url_prefix="/cb_controller")


app.run(debug=True)
