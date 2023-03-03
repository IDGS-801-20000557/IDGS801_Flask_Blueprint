from flask import Blueprint

maestros=Blueprint('maestros',__name__)

@maestros.route('/getmaes', methods=['GET'])
def getMaes():
    return {'key':'Maestros'}
