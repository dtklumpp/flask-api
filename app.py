import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
# print(__name__)

# Set Base Directory
basedir = os.path.abspath(os.path.dirname(__file__))

# SQLite Database
# DATABASE = 'sqlite:///' + os.path.join(basedir, 'db.reddit')

# Local Postgres Database
DATABASE = 'postgresql://localhost/redditdb'

# Setup Database
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init Database
db = SQLAlchemy(app)

#Init Marshmallow
marshmallow = Marshmallow(app)




DEBUG = True
PORT = 8001

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    from models import Sub
    return 'Hello'

@app.route('/sub')


@app.route('/sub/', methods=['GET', 'POST'])
@app.route('/sub/<subid>/', methods=['GET'])
def get_or_create_sub(subid=None):
    from models import Sub
    if subid == None and request.method == 'GET':
        return Sub.get_subs()
    elif subid == None and request.method == 'POST':
        name = request.json["name"]
        description = request.json["description"]
        return Sub.create_sub(name, description)
    else:
        return Sub.get_sub(subid)


@app.route('/sub/<subid>/', methods=['PUT'])
def update_sub(subid):
    from models import Sub
    data = request.get_json()
    return Sub.update_sub(subid, **data)



@app.route('/sub/<subid>/', methods=['DELETE'])
def delete_sub(subid):
    from models import Sub
    return Sub.delete_sub(subid)

if __name__ == '__main__':
	app.run(debug=DEBUG, port=PORT)