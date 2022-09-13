#-------------------------------------------------------------------#
from urllib import request
from flask import jsonify, request,json
from flask import Blueprint
from models.estudiantes import estudiantes
from utils.db import db
from models.order import orde
#-------------------------------------------------------------------#
routes=Blueprint('routes',__name__)
#---------------------AÑADIR ESTUDIANTE----------------------------------------------#
@routes.route("/estudiante/add",methods=['POST'])
def add_estudiante():
    try:
        body=json.loads(request.data)
        cedula=body['cedula']
        nombre=body['nombre']
        apellido=body['apellido']
        edad=body['edad']
        new_add=estudiantes(cedula,nombre,apellido,edad)
        db.session.add(new_add)
        db.session.commit()
        return jsonify({'message': 'Estudiante Añadido'})
    except Exception as error:
        return jsonify({'message': 'Error al añadir estudiante'})    
#-----------------------BORRAR ESTUDIANTE--------------------------------------------#
@routes.route("/estudiante/delete/<int:id>",methods=['GET'])
def delete(id):
    try:
        estudi=estudiantes.query.get(id)
        db.session.delete(estudi)
        db.session.commit()
        return jsonify({'message': 'USUARIO BORRADO'})   
    except Exception as error:
        return jsonify({'message': 'Error al Borrar Estudiante'})
#--------------------------VISUALITAR ESTUDIANTE TOTALES-----------------------------------------#
@routes.route("/estudiante/view",methods=['GET'])
def vista_estudiante():
    try:
        listado=[]
        estudiantes_all=estudiantes.query.all()
        for i in estudiantes_all:
            full_estudiantes=orde(i.cedula,i.nombre,i.apellido,i.edad)
            listado.append(full_estudiantes)
        return jsonify({"Estudiantes Encontrados": listado})
    except Exception as error:
        return jsonify({'message': 'Error al Buscar Estudiante'})
#----------------------------BUSCAR POR APELLIDO LOS ESTUDIANTES---------------------------------------#
@routes.route("/estudiante/search/<string:ListaEst_Apellido>",methods=['GET'])
def search_estudiante(ListaEst_Apellido):
    try:
        ListaEst=estudiantes.query.all()
        listado=[]
        for i in ListaEst:
            ape_estudiantes=orde(i.cedula,i.nombre,i.apellido,i.edad)
            if i.apellido == ListaEst_Apellido:
                listado.append(ape_estudiantes)
        return jsonify({"Estudiantes Encontrados": listado})
    except Exception as error:
        return jsonify({'message': 'Error al Buscar Estudiante'})
#--------------------------EDITAR LOS ESTUDIANTES-----------------------------------------#
@routes.route("/estudiante/edit/<int:id>",methods=['POST'])
def edit_estudiante(id):
    estudi=estudiantes.query.get(id)
    try:
        body=json.loads(request.data)
        estudi.cedula=body['cedula']
        estudi.nombre=body['nombre']
        estudi.apellido=body['apellido']
        estudi.edad=body['edad']
        db.session.commit()
        return jsonify({'message': 'Estudiante Actualizado'})
    except Exception as error:
        return jsonify({'message': 'Error al actualizar estudiante'})
#-------------------------------------------------------------------#