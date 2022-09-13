from flask_sqlalchemy import SQLAlchemy
from utils.db import db
#-------------------------------------------------------------------#
class estudiantes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    cedula=db.Column(db.String(10),unique=True)
    nombre=db.Column(db.String(100))
    apellido=db.Column(db.String(100))
    edad=db.Column(db.Integer)
    #-------------------------------------------------------------------#
    def __init__(self,cedula,nombre,apellido,edad):
        self.cedula=cedula
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
    #-------------------------------------------------------------------#    