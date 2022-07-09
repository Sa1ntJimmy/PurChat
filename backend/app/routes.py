
from requests import request
from backend.app.models import Users
from backend.main import app, app_db
from flask import jsonify

@app.route('/users')
def users():
    return jsonify(Users.query.all())

@app.route('/users/<int:userid>')
def user_from_userid(userid):
    return jsonify(Users.query.get(userid))

@app.route('/users/<string:username>')
def user_from_username(username):
    return jsonify(Users.query.filter(Users.username==username).first())

@app.route('/new_user', methods=["POST"])
def new_user():
    user = Users(username=request.form["username"])
    app_db.session.add(user)
    app_db.session.commit()
