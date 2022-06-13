
from backend.app.models import Users
from backend.main import app
from flask import jsonify
from markupsafe import escape

@app.route('/user')
def user():
    return jsonify(Users.query.all())

@app.route('/user/<username>')
def user_from_username(username):
    return jsonify(Users.query.filter(Users.userid == 1))