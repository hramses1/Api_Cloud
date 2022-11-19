from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from routes.routes import routes

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]='*********'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
SQLAlchemy(app)

app.register_blueprint(routes)

