from flask_sqlalchemy import SQLAlchemy

def init_db(app):
    db_name = './database.db'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    return SQLAlchemy(app)

def close_db(db):
    db.Close()