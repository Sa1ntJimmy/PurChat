from flask import Flask
import backend.db as db

app = Flask(__name__)

app_db = db.init_db(app)

@app.route('/')
def index():
    return "Flask has been started succesfully!"

from backend.app.routes import user_from_username

if __name__ == '__main__':
    app.run(debug=True)