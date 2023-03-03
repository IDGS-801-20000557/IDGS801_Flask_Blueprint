from flask import Flask, render_template, jsonify
from flask import request
from flask import redirect
from flask import url_for

from alumnos.routes import alumnos
from directivos.routes import dir
from maestros.routes import maestros

app=Flask(__name__)
app.config['DEBUG']=True


@app.route("/", methods=['GET'])
def home():
    return jsonify({'Datos':'Hola'})


app.register_blueprint(alumnos)
app.register_blueprint(dir)
app.register_blueprint(maestros)


if __name__ =='__main__':
    app.run()
