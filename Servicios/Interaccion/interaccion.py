from Datos.Modelos import Consultas as modelo_consultas
from Datos.Modelos import Respuestas as modelo_respuestas
from Datos.Modelos import Foros as modelo_foros


# # # # # # #
# CONSULTA  #
# # # # # # #

def obtener_consultas():
    return modelo_consultas.obtener_consultas()

def obtener_consulta(parecido, ID_UsuarioC):
    consulta = modelo_consultas.obtener_consulta(parecido, ID_UsuarioC)
    if len(consulta) == 0:
        raise Exception('No existe tal consulta')
    return consulta

def crear_consulta(ID_UsuarioC, Q, F, P, Liter, Leng, I, M, A, B, O, Consulta):
    modelo_consultas.crear_consulta(ID_UsuarioC, Q, F, P, Liter, Leng, I, M, A, B, O, Consulta)

def modificar_consulta(IDConsulta, datos_consulta):
    modelo_consultas.modificar_consulta(IDConsulta, datos_consulta)

def borrar_consulta(IDConsulta):
    modelo_consultas.borrar_consulta(IDConsulta)


# # # # # # # #
# RESPUESTAS  #
# # # # # # # #

def responder_consulta(IDc, ID_UsuarioR, Respuesta, fecha):
    modelo_respuestas.responder_consulta(IDc, ID_UsuarioR, Respuesta, fecha)

def borrar_respuesta(ID):
    modelo_respuestas.borrar_respuesta(ID)

def modificar_respuesta(ID, datos_respuesta):
    modelo_respuestas.modificar_respuesta(ID, datos_respuesta)

def obtener_Resp():
    return modelo_respuestas.obtener_respuestas()


# # # # #
# FOROS #
# # # # #

def obtener_foros():
    return modelo_foros.obtener_foros()

def obtener_foro(ID_foro):
    consultaCompleta = modelo_foros.obtener_foro(ID_foro)
    if len(consultaCompleta) == 0:
        raise Exception('No existe tal consulta')
    return consultaCompleta[0]

def crear_foro(UsuarioCuestiona, Consulta, UsuarioResponde, Respuesta, Estado):
    modelo_foros.crear_foro(UsuarioCuestiona, Consulta, UsuarioResponde, Respuesta, Estado)