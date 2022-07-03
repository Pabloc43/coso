from flask import Flask, request, jsonify, render_template
from Servicios.Autenticacion import Autenticacion
from Servicios.Interaccion import interaccion
from Servicios.Mascota import botMascota

app = Flask(__name__)


# Inicio
@app.route('/')
def get_index():
    titulo_verduleria = 'Studyngo!!'
    return render_template('login.html', titulo=titulo_verduleria)


# # # # # #
# USUARIO #
# # # # # #

@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    datos_usuario = request.get_json()
    Lista_campos_usuario = ['A_tematicas', 'Genero', 'NombreUsuario', 'email', 'FechaNacimiento', 'Contrasenia']
    for campo in Lista_campos_usuario:
        if campo not in datos_usuario or datos_usuario[campo] == '':
            return f'El campo {campo} es requerido', 412
    try:
        Autenticacion.crear_usuario(
            datos_usuario['A_tematicas'], datos_usuario['Genero'], datos_usuario['NombreUsuario'],
            datos_usuario['email'], datos_usuario['FechaNacimiento'], datos_usuario['Contrasenia'])
    except Exception:
        return 'El nombre de usuario o email no estan disponibles', 409
    return 'OK', 200


@app.route('/usuarios/<IDUsuario>', methods=['PUT'])
def modificar_usuario(IDUsuario):
    datos_usuario = request.get_json()
    Lista_campos_usuario = ['A_tematicas', 'Genero', 'NombreUsuario', 'email', 'FechaNacimiento', 'Contrasenia']
    for campo in Lista_campos_usuario:
        if campo not in datos_usuario or datos_usuario[campo] == '':
            return f'El campo {campo} es requerido', 412
    try:
        Autenticacion.modificar_usuario(IDUsuario, datos_usuario)
    except Exception:
        return 'El nombre de usuario o email no estan disponibles', 409
    return 'OK', 200


@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(Autenticacion.obtener_usuarios())


@app.route('/usuarios/<IDUsuario>', methods=['GET'])
def obtener_usuario(IDUsuario):
    # try:
    usuario = Autenticacion.obtener_usuario(IDUsuario)
    return jsonify(usuario)


# except Exception:
# return 'Usuario no encontrado', 404


@app.route('/usuarios/<IDUsuario>', methods=['DELETE'])
def borrar_usuario(IDUsuario):
    Autenticacion.borrar_usuario(IDUsuario)
    return 'Borrado', 200


@app.route('/login', methods=['POST'])
def login():
    datos_usuario = request.get_json()
    if ('NombreUsuario' or 'Contrasenia') not in datos_usuario or (
            datos_usuario['NombreUsuario'] == '' or datos_usuario['Contrasenia'] == ''):
        return 'El nombre de usuario o la contraseña son requeridos', 412
    try:
        id_sesion = Autenticacion.login(datos_usuario['NombreUsuario'], datos_usuario['Contrasenia'])
        return jsonify({"id_sesion": id_sesion})
    except Exception:
        return 'Usuario no encontrado', 404


# CUESTIONARIO INICIAL
@app.route('/C_inicial', methods=['POST'])
def C_inicial():
    datos_cuestionario = request.get_json()
    Lista_campos_cuestionario = ['User', 'N_estudio', 'A_bien', 'A_mal']
    for campo in Lista_campos_cuestionario:
        if campo not in datos_cuestionario or datos_cuestionario[campo] == '':
            return f'El campo {campo} es requerido', 412
    try:
        Autenticacion.C_inicial(
            datos_cuestionario['User'], datos_cuestionario['N_estudio'], datos_cuestionario['A_bien'],
            datos_cuestionario['A_mal'])
    except Exception:
        return 'Algo salio mal', 409
    return 'OK', 200


# # # # # # #
# CONSULTAS #
# # # # # # #

@app.route('/consultas', methods=['POST'])
def crear_consulta():
    datos_consulta = request.get_json()
    Lista_campos_consulta = ['ID_UsuarioC', 'Consulta']
    for campo in Lista_campos_consulta:
        if campo not in datos_consulta or datos_consulta[campo] == '':
            return f'El campo {campo} es requerido', 412
    try:
        interaccion.crear_consulta(
            datos_consulta['ID_UsuarioC'], datos_consulta['Q'], datos_consulta['F'], datos_consulta['P'],
            datos_consulta['Liter'], datos_consulta['Leng'], datos_consulta['I'], datos_consulta['M'],
            datos_consulta['A'], datos_consulta['B'], datos_consulta['O'], datos_consulta['Consulta'])
    except Exception:
        return 'Ocurrio un error, intente de nuevo', 500
    return 'OK', 200


@app.route('/consultas/particular', methods=['GET'])
def obtener_consulta():
    datos_consulta = request.get_json()
    if ('ID_UsuarioC' or 'Consulta') not in datos_consulta or (
            datos_consulta['ID_UsuarioC'] == '' or datos_consulta['Consulta'] == ''):
        return 'El nombre de usuario o la contraseña son requeridos', 412
    try:
        consulta = interaccion.obtener_consulta(datos_consulta['Consulta'], datos_consulta['ID_UsuarioC'])
        return jsonify(consulta)
    except Exception:
        return 'Consulta no encontrada', 404


@app.route('/consultas', methods=['GET'])
def obtener_consultas():
    return jsonify(interaccion.obtener_consultas())


@app.route('/consultas/<IDConsulta>', methods=['DELETE'])
def borrar_consulta(IDConsulta):
    interaccion.borrar_consulta(IDConsulta)
    return 'Borrada', 200


@app.route('/consultas/<IDConsulta>', methods=['PUT'])
def modificar_consulta(IDConsulta):
    datos_consulta = request.get_json()
    Lista_campos_consulta = ['Consulta', 'Estado'] #deberia agregar mas, pero lo gestiono en web
    for campo in Lista_campos_consulta:
        if campo not in datos_consulta or datos_consulta[campo] == '':
            return f'El campo {campo} es requerido', 412
    try:
        interaccion.modificar_consulta(IDConsulta, datos_consulta)
    except Exception:
        return 'No se encontro la duda a modificar', 404
    return 'OK', 200


# # # # # # # #
# RESPUESTAS  #
# # # # # # # #

@app.route('/respuestas', methods=['POST'])
def responder_consulta():
    datos_respuesta = request.get_json()
    Lista_campos_respuesta = ['IDc', 'ID_UsuarioR', 'Respuesta', 'Fecha']
    for campo in Lista_campos_respuesta:
        if campo not in datos_respuesta or datos_respuesta[campo] == '':
            return f'El campo {campo} es requerido', 412
    try:
        interaccion.responder_consulta(
            datos_respuesta['IDc'], datos_respuesta['ID_UsuarioR'], datos_respuesta['Respuesta'], datos_respuesta['Fecha'])
    except Exception:
        return 'Ocurrio un error, intente de nuevo', 500
    return 'OK', 200


@app.route('/respuestas/<ID>', methods=['DELETE'])
def borrar_respuesta(ID):
    interaccion.borrar_respuesta(ID)
    return 'Borrada', 200


@app.route('/respuestas/<ID>', methods=['PUT'])
def modificar_respuesta(ID):
    datos_respuesta = request.get_json()
    Lista_campos_respuesta = ['Respuesta']
    for campo in Lista_campos_respuesta:
        if campo not in datos_respuesta or datos_respuesta[campo] == '':
            return f'El campo {campo} es requerido', 412
    try:
        interaccion.modificar_respuesta(ID, datos_respuesta)
    except Exception:
        return 'No se encontro tal duda a modificar', 404
    return 'OK', 200


@app.route('/respuestas', methods=['GET'])
def obtener_resp():
    return jsonify(interaccion.obtener_Resp())

# # # # #
# FOROS #
# # # # #

@app.route('/foros', methods=['POST'])
def crear_foros():
    datos_foros = request.get_json()
    Lista_campos_foros = ['UsuarioCuestiona', 'Consulta', 'UsuarioResponde', 'Respuesta']
    for campo in Lista_campos_foros:
        if campo not in datos_foros or datos_foros[campo] == '':
            return f'El campo {campo} es requerido', 412
    try:
        interaccion.crear_foro(
            datos_foros['UsuarioCuestiona'], datos_foros['Consulta'], datos_foros['UsuarioResponde'],
            datos_foros['Respuesta'], datos_foros['Estado'])
    except Exception:
        return 'Ocurrio un error, intente de nuevo', 500
    return 'OK', 200


@app.route('/foros/<IDforo>', methods=['GET'])
def obtener_foro(IDforo):
    try:
        foro = interaccion.obtener_foro(IDforo)
        return jsonify(foro)
    except Exception:
        return 'Foro no encontrada', 404


@app.route('/foros', methods=['GET'])
def obtener_foros():
    return jsonify(interaccion.obtener_foros())


# # # #
# BOT #
# # # #

@app.route('/bot', methods=['POST'])
def crear_bot():
    datos_bot = request.get_json()
    Lista_campos_bot = ['Apodo', 'Apariencia']
    for campo in Lista_campos_bot:
        if campo not in datos_bot or datos_bot[campo] == '':
            return f'El campo {campo} es requerido', 412
    try:
        botMascota.crear_bot(
            datos_bot['Apodo'], datos_bot['Apariencia'])
    except Exception:
        return 'Ocurrio un error, intente de nuevo', 500
    return 'OK', 200


@app.route('/bot/<ID>', methods=['PUT'])
def modificar_bot(ID):
    datos_bot = request.get_json()
    Lista_campos_bot = ['Apodo', 'Apariencia']
    for campo in Lista_campos_bot:
        if campo not in datos_bot or datos_bot[campo] == '':
            return f'El campo {campo} es requerido', 412
    try:
        botMascota.modificar_bot(ID, datos_bot)
    except Exception:
        return 'No se encontro tal duda a modificar', 404
    return 'OK', 200


@app.route('/bot/<IDConsulta>', methods=['GET'])
def obtener_bot(IDbot):
    try:
        bot = botMascota.obtener_bot(IDbot)
        return jsonify(bot)
    except Exception:
        return 'Consulta no encontrada', 404


# # # # #
# AYUDA #
# # # # #


@app.route('/ayudafU', methods=['POST'])
def crear_MCF():
    datos_Mconsulta = request.get_json()
    if 'Cuestion' not in datos_Mconsulta or datos_Mconsulta['Cuestion'] == '':
        return 'El campo "Cuestion" es requerido', 412
    try:
        Autenticacion.crear_MCF(
            datos_Mconsulta['Cuestion'])
    except Exception:
        return 'No se pudieron cargar los datos', 409
    return 'OK', 200

@app.route('/ayudafA/<IDc>', methods=['PUT'])
def modificar_MCF(IDc):
    datos_Mconsulta = request.get_json()
    if 'rCuestion' not in datos_Mconsulta or datos_Mconsulta['rCuestion'] == '':
            return 'El campo "rCuestion" es requerido', 412
    try:
        Autenticacion.modificar_MCF(IDc, datos_Mconsulta)
    except Exception:
        return 'No se guardo la respuesta', 409
    return 'OK', 200


@app.route('/ayudafU/<parecido>', methods=['GET'])
def obtener_MCDU(parecido):
    return jsonify(Autenticacion.obtener_MCFU(parecido))


@app.route('/ayudafA/<IDc>', methods=['GET'])
def obtener_MCFA(IDc):
    return jsonify(Autenticacion.obtener_MCFA(IDc))


@app.route('/ayudafA/<IDc>', methods=['DELETE'])
def borrar_MCF(IDc):
    Autenticacion.eliminar_MCF(IDc)
    return 'Borrado', 200


if __name__ == '__main__':
    app.debug = True
    app.run(port=5008)
