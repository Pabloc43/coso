from Datos.Modelos import Usuario as modelo_usuario
from datetime import datetime
from Datos.Modelos import Ayuda_foro as help

def _existe_usuario(NombreUsuario, Contrasenia):
    usuarios = modelo_usuario.obtener_usuarios_por_NombreUsuario_Contrasenia(NombreUsuario, Contrasenia)
    return not len(usuarios) == 0


def _crear_sesion(IDUsuario):
    hora_actual = datetime.now()
    # dd/mm/YY = H:M:S
    dt_string = hora_actual.strftime('%d/%m/%Y %H:%M:%S')
    return modelo_usuario.crear_sesion(IDUsuario, dt_string)


def obtener_usuarios():
    return modelo_usuario.obtener_usuarios()


def obtener_usuario(IDUsuario):
    usuarios = modelo_usuario.obtener_usuario(IDUsuario)
    if len(usuarios) == 0:
        raise Exception('El usuario no existe')
    return usuarios[0]


def crear_usuario(A_tematicas, Genero, NombreUsuario, email, FechaNacimiento, Contrasenia):
    if not _existe_usuario(NombreUsuario, Contrasenia):
        modelo_usuario.crear_usuario(A_tematicas, Genero, NombreUsuario, email, FechaNacimiento, Contrasenia)
    else:
        raise Exception('El usuario ya existe')


def modificar_usuario(IDUsuario, datos_usuario):
    modelo_usuario.modificar_usuario(IDUsuario, datos_usuario)


def borrar_usuario(IDUsuario):
    modelo_usuario.borrar_usuario(IDUsuario)


def login(NombreUsuario, Contrasenia):
    if _existe_usuario(NombreUsuario, Contrasenia):
        usuario = modelo_usuario.obtener_usuarios_por_NombreUsuario_Contrasenia(NombreUsuario, Contrasenia)[0]
        return _crear_sesion(usuario['IDUsuario'])
    else:
        raise Exception('El usuario no existe o la contrasenia es invalida')


def validar_sesion(id_sesion):
    sesiones = modelo_usuario.obtener_sesion(id_sesion)
    if len(sesiones) == 0:
        return False
    elif (datetime.now() - datetime.strptime(sesiones[0]['fecha_hora'], "%d/%m/%Y %H:%M:%S")).total_seconds() > 7200:
        return False
    else:
        return True


def C_inicial(User, N_estudio, A_bien, A_mal):
    modelo_usuario.C_inicial(User, N_estudio, A_bien, A_mal)

#########
# AYUDA #
#########
#1AYUDAD
#...
#2AYUDAF
#2.1 USER
def obtener_MCFU(parecido):
    return help.obtener_MCFU(parecido)

def crear_MCF(Cuestion):
    help.crear_MCF(Cuestion)
#2.2 ADMIN
def eliminar_MCF(IDc):
    help.borrar_MconsultaF(IDc)

def modificar_MCF(IDc, datos_Mconsulta):
    help.modificar_MCF(IDc, datos_Mconsulta)

def obtener_MCFA(IDc):
    return help.obtener_MCFA(IDc)