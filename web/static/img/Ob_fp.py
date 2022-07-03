##ACTUALMENTE BASURERO
###FUTURAMENTE PROGRAMA QUE SE ENCARGUE DE GUARDAR Y AYUDE A SERVIR FOTO DE USUARIO POR MEDIO DE SU URL


import os
import requests
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from web.servidor_web import app


UPLOAD_FOLDER = '/p_img'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




def hacercosourl():
    pass

def hacercosoobtenerimgporIDenAPI():
    pass
"""NO FUNCIONO, PARA CUMPLIR LO MEJOR POSIBLE SE TRATA LUEGO
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
UPLOAD_FOLDER = 'static/img/p_img'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/registro', methods=['GET', 'POST'])
def upload_file():
    error = None
    if request.method == 'POST':
        if not autenticacion.crear_usuario(request.form['intereses'], request.form['genero'], request.form['login'],
                                           request.form['file'],
                                           request.form['email'], request.form['fecha'], request.form['password']):
            error = 'No se pudo crear el usuario'
        else:
            return redirect(url_for('inicio'))
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
    return render_template('registro.html', error=error)
"""