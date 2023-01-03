from flask import Flask
import backend.db as db
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

app_db = db.init_db(app)

@app.route('/')
def index():
    return "Flask has been started succesfully!"

from backend.app.routes import users, user_from_userid, user_from_username

if __name__ == '__main__':
    app.run(debug=True)