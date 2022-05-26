from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from jinja2 import Template

app = Flask(__name__)

# change to name of your database; add path if necessary
db_name = 'database.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)

class Users(db.Model):
    userid = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    username = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<username: %r>' % self.username

# NOTHING BELOW THIS LINE NEEDS TO CHANGE
# this route will test the database connection and nothing more
@app.route('/')
def testdb():
    try:
        user = Users.query.get(2)
        return str(user.username)
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text



if __name__ == '__main__':
    app.run(debug=True)