from flask import Flask, Response, request, render_template
from tinydb import TinyDB, Query
from flask_restful import Api, Resource
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth
import pandas as pd
import json
import bcrypt

app = Flask(__name__)
api = Api(app)
CORS(app)
auth = HTTPBasicAuth()

@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    db = TinyDB('./db.json')
    user = Query()
    result = db.search(user.email == username)
    if len(result) != 0:
        hash = result[0]["password"]
        if bcrypt.checkpw(password.encode("utf-8"), hash.encode("utf-8")):
            return True
        else:
           return False
    else:
        return False

class User(Resource):
    def post(self):
        db = TinyDB('./db.json')
        user = Query()
        param = request.get_json()
        email = param["email"]
        password = param["password"]
        new_user = param["new_user"]
        if new_user == False:
            result = db.search(user.email == email)
            if len(result) != 0:
                email = result[0]["email"]
                hash = result[0]["password"]
                if bcrypt.checkpw(password.encode("utf-8"), hash.encode("utf-8")):
                    response = Response(status=200) #match
                    return response
                else:
                    response = Response(status=401) #no match (Unauthorized)
                    return response
            else:
                response = Response(status=401) #no id
                return response
        elif new_user == True:
            hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            db.insert({'email': email, 'password': hashed.decode("utf-8")})
            response = Response(status=201)
            return response

api.add_resource(User, '/login')

@app.route('/')
def hello():
    """Renders a sample page."""
    return "Hello Friend!"

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)