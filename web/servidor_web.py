import datetime
import json
from json import JSONDecodeError

from flask import Flask, request, redirect, url_for, session
from flask import render_template
from werkzeug.exceptions import BadRequestKeyError

from web.servicios import autenticacion

app = Flask(__name__)
app.secret_key = 'claveDificil123'


@app.route('/')
def cambio_Ruta():
    return redirect(url_for('inicio'))


@app.route('/inicio')
def inicio():
    return render_template('inicio.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if not autenticacion.validar_credenciales(request.form['login'], request.form['password']):
            error = 'Credenciales inválidas'
        else:
            session['user'] = request.form['login']
            return redirect(url_for('general'))
    else:
        if 'user' in session:
            return render_template('salidas2.html')
    return render_template('login.html', error=error)


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    error = None
    if request.method == 'POST':
        if not autenticacion.crear_usuario(request.form['intereses'], request.form['genero'], request.form['login'],
                                           request.form['email'], request.form['fecha'], request.form['password']):
            error = 'No se pudo crear el usuario'
        else:
            session['user'] = request.form['login']
            return redirect(url_for('C_inicial'))
    else:
        if 'user' in session:
            return render_template('salidas2.html')
    return render_template('registro.html', error=error, data=[{'genero': 'Sin especificar'},
                                                               {'genero': 'Masculino'},
                                                               {'genero': 'Femenino'},
                                                               {'genero': 'Otro'}])


@app.route('/registro/C_inicial', methods=['GET', 'POST'])
def C_inicial():
    error = None
    if 'user' in session:
        if request.method == 'POST':
            try:
                usuario = session['user']
                if not autenticacion.C_inicial(usuario, request.form['primero'], request.form['segundo'],
                                               request.form['tercero']):
                    error = 'Ocurrio un error al ingresar los datos, revise sin completo bien los campos'
                else:
                    return redirect(url_for('general'))
            except:
                error = 'Complete todos los campos'
                return render_template('C_inicial.html', error=error)
        if request.method == 'GET':
            areas = [{'area': 'Quimica'}, {'area': 'Fisica'}, {'area': 'Programacion'}, {'area': 'Literatura'},
                     {'area': 'Lenguas'}, {'area': 'Ingles'}, {'area': 'Matematicas'}, {'area': 'Astronimia'},
                     {'area': 'Biologia'}, {'area': '...agregar mas'}]
            return render_template('C_inicial.html',
                                   level=[{'estudios': 'Primaria incompleta'}, {'estudios': 'Primaria completa'},
                                          {'estudios': 'Secundaria incompleta'}, {'estudios': 'Secundaria completa'},
                                          {'estudios': 'Doctorado'}, {'estudios': 'Autodidacta'},
                                          {'estudios': 'Estudios de grado'}, {'estudios': '...añadir mas opciones'},
                                          {'estudios': 'Otro'}], areas=areas, error=error)
    else:
        return render_template('salidas.html')


# PRJRJJRFJRJGJGRJJRJVJJRVJJVJR
@app.route('/general', methods=['GET', 'POST'])
def general():
    if 'user' in session:
        if request.method == 'GET':
            datos_usuario = session['user']
            a = autenticacion.obtener_AllConsultas()
            liss = autenticacion.obtener_AllConsultas()
            comm = autenticacion.obtener_comentarios()
            lisss = []
            for i in liss:
                if liss != None and i['ID_UsuarioC'] != datos_usuario:
                    lisss.append(i)
            lis = []
            for i in a:
                if a != None and i['ID_UsuarioC'] == datos_usuario:
                    lis.append(i)
            coment = []
            for i in comm:
                for l in liss:
                    if comm != None and i['IDc'] == l['IDc']:
                        coment.append(i)
            commi = []
            for i in comm:
                for l in lis:
                    if comm != None and i['IDc'] == l['IDc']:
                        commi.append(i)
            liss.reverse()
            a.reverse()
            return render_template('home.html', lis=lis, lisss=lisss, coment=coment, session=session, commi=commi)
            # return render_template('general.html')
        if request.method == 'POST':
            try:

                if not autenticacion.crear_comentario(request.form['IDc'], session['user'],
                                                      request.form['Respuesta'],
                                                      datetime.datetime.strftime(datetime.datetime.now(),
                                                                                 '%d/%m/%Y %H:%M:%S')):
                    error = 'Ocurrio un error al ingresar los datos, revise sin completo bien los campos'
                    return render_template('home.html', error=error, session=session)
                else:
                    return redirect(url_for('general'))
            except (JSONDecodeError, BadRequestKeyError):
                try:
                    if not autenticacion.eliminar_Com(request.form['IDD']):
                        error = 'Comuniquenos su error'
                        return render_template('home.html', error=error, session=session)
                except:
                    return redirect(url_for('general'))
    return render_template('salidas.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('inicio'))


@app.route('/nosotros', methods=['GET', 'POST'])
def nosotros():
    return render_template('nosotros.html')


@app.route('/ayuda', methods=['GET', 'POST'])
def ayudaF():
    error = None
    if request.method == 'POST':
        try:
            if not autenticacion.crear_MCF(request.form['Cuestion']):
                error = 'Ingrese una duda antes de enviar'
            else:
                error = 'Consulta guardada exitosamente, busque a ver si ya esta su respuesta.'
            return render_template('ayuda.html', error=error)
        except:
            if not autenticacion.obtener_MCF(request.form['buscar']):
                error = 'Ingrese algo'
            else:
                coincidencias = autenticacion.obtener_MCF(request.form['buscar'])
                return render_template('ayuda.html', coincidencias=coincidencias, error=error)
    return render_template('ayuda.html', error=error)


# error = None


@app.route('/usuario', methods=['GET', 'POST'])
def usuario():
    error = None
    if 'user' in session:
        datos_usuario = session['user']
        a = autenticacion.obtener_usuarios()
        bandera = True
        i = 0
        while bandera == True:
            if a[i]['NombreUsuario'] == datos_usuario:
                usuario = a[i]
                claveusuario = ['NombreUsuario', 'Genero', 'A_tematicas', 'email', 'FechaNacimiento', 'IDUsuario',
                                'Contrasenia']
                if request.method == 'GET':
                    return render_template('usuario.html', usuario=usuario, claveusuario=claveusuario,
                                           data=[{'genero': 'Sin especificar'},
                                                 {'genero': 'Masculino'},
                                                 {'genero': 'Femenino'},
                                                 {'genero': 'Otro'}])
                elif request.method == 'POST':
                    try:
                        autenticacion.modificar_user(usuario['IDUsuario'], request.form['intereses'],
                                                     request.form['genero'], usuario['NombreUsuario'],
                                                     request.form['email'], request.form['fecha'],
                                                     request.form['password'])
                        return redirect(url_for('usuario'))
                    except:
                        if not autenticacion.obtener_MCF(request.form['buscar']):
                            error = 'Ingrese algo'
                        else:
                            coincidencias = autenticacion.obtener_MCF(request.form['buscar'])
                            return render_template('usuario.html', coincidencias=coincidencias, error=error)
                elif request.method == 'DELETE':
                    pass
            else:
                i = i + 1
                if i > len(a):
                    bandera = False
            # return render_template('general.html')
    else:
        return render_template('salidas.html')


@app.route('/consulta', methods=['GET', 'POST'])
def consulta():
    error = None
    if 'user' in session:
        if request.method == 'POST':
            try:
                lista = ['Quimica', 'Fisica', 'Programacion', 'Literatura', 'Lenguas', 'Ingles',
                         'Matematicas', 'Astronomia', 'Biologia', 'Otro']
                i = 0
                for item in lista:
                    if (item in request.form.keys()):
                        lista[i] = int(request.form[item])
                        i = i + 1
                    else:
                        lista[i] = 0
                        i = i + 1
                if not autenticacion.crear_consulta(session['user'], lista[0], lista[1], lista[2], lista[3], lista[4],
                                                    lista[5], lista[6], lista[7], lista[8], lista[9],
                                                    request.form['Consulta']):
                    error = 'Hubo un error, intente de nuevo, o informenos en la pestaña ayuda'
                    return render_template('consulta.html', error=error)
                else:
                    error = 'Consulta guardada exitosamente, busque a ver si ya fue respondida.'
                    return render_template('consulta.html', error=error)
            except BadRequestKeyError:
                try:
                    try:
                        if not autenticacion.obtener_Consultas(request.form['buscar'], session['user']):
                            error = 'Ingrese algo'
                            return render_template('consulta.html', error=error)
                        else:
                            coincidencias = autenticacion.obtener_Consultas(request.form['buscar'], session['user'])
                            areas = [{'area': 'Quimica'}, {'area': 'Fisica'}, {'area': 'Programacion'},
                                     {'area': 'Literatura'},
                                     {'area': 'Lenguas'}, {'area': 'Ingles'}, {'area': 'Matematicas'},
                                     {'area': 'Astronomia'},
                                     {'area': 'Biologia'}, {'area': 'Otro'}]
                            return render_template('consulta.html', coincidencias=coincidencias, error=error,
                                                   areas=areas)
                    except json.JSONDecodeError:
                        error = 'No hay concidencias'
                        return render_template('consulta.html', error=error)
                except:
                    try:
                        if not autenticacion.eliminar_Consulta(int(request.form['Eliminar'])):
                            error = 'Comuniquenos cual es el error'
                            return render_template('consulta.html', error=error)
                        else:
                            error = 'Se elimino exitosamente'
                            return render_template('consulta.html', error=error)
                    except:
                        listaU = ['up-Quimica', 'up-Fisica', 'up-Programacion', 'up-Literatura', 'up-Lenguas',
                                  'up-Ingles',
                                  'up-Matematicas', 'up-Astronomia', 'up-Biologia', 'up-Otro', 'Estado']
                        i = 0
                        for item in listaU:
                            if (item in request.form.keys()):
                                listaU[i] = int(request.form[item])
                                i = i + 1
                            else:
                                listaU[i] = 0
                                i = i + 1
                    try:
                        if not autenticacion.modificar_Consulta(request.form['identificador'], session['user'],
                                                                listaU[0], listaU[1], listaU[2],
                                                                listaU[3], listaU[4], listaU[5], listaU[6], listaU[7],
                                                                listaU[8], listaU[9],
                                                                request.form['up-Consulta'], listaU[10]):
                            error = 'Ingrese un nombre distintivo en el buscador por coincidencias'
                            return render_template('consulta.html', error=error)
                        else:
                            error = 'Consulta guardada exitosamente, busque a ver si ya esta su respuesta'
                            return render_template('consulta.html', error=error)
                    except (BadRequestKeyError, TypeError):
                        error = [
                            'Eliminar: Eliminado exitosamente.  ' 'Modificar: Verificar haber marcado el checkbox para editar.']
                        return render_template('consulta.html', error=error[0])
        if request.method == 'GET':
            areas = [{'area': 'Quimica'}, {'area': 'Fisica'}, {'area': 'Programacion'}, {'area': 'Literatura'},
                     {'area': 'Lenguas'}, {'area': 'Ingles'}, {'area': 'Matematicas'}, {'area': 'Astronomia'},
                     {'area': 'Biologia'}, {'area': 'Otro'}]
            return render_template('consulta.html', areas=areas)
    else:
        return render_template('salidas.html')


# if request.method == 'POST':
#    if not autenticacion.crear_MCF(request.form['Cuestion']):
#       error = 'Ingrese una duda antes de enviar'
#   else:
#       error = 'Consulta guardada exitosamente, aguarde su respuesta'
#       return render_template('ayuda.html', error=error)
#   return render_template('ayuda.html', error=error)
# if not autenticacion.crear_MCF(request.form['Cuestion']):
#     error = 'Ingrese una duda antes de enviar'
# elif autenticacion.obtener_MCF(request.form['buscar']):
#     parecido = request.form['buscar']
#     coincidencias = autenticacion.obtener_MCF(parecido)
#     return render_template('ayuda.html', coincidencias=coincidencias)
# else:
#     error = 'Consulta guardada exitosamente, aguarde su respuesta'
# return render_template('ayuda.html', error=error)
# return render_template('ayuda.html', error=error)


# if request.method == 'GET':
# parecido = request.form['parecido']
# listaDiccio = autenticacion.obtener_MCF(parecido)
#   return render_template('ayuda.html', error=error)#, listaDiccio=listaDiccio)

if __name__ == '__main__':
    app.debug = True
    app.run(port=5007)
