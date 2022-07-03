import requests
from web.servicios import rest_api


def validar_credenciales(usuario, clave):
    body = {"NombreUsuario": usuario,
            "Contrasenia": clave}
    respuesta = requests.post(f'{rest_api.API_URL}/login', json=body)
    return respuesta.status_code == 200


def crear_usuario(A_tematicas, Genero, NombreUsuario, email, FechaNacimiento, Contrasenia):
    body = {"A_tematicas": A_tematicas,
            "Genero": Genero,
            "NombreUsuario": NombreUsuario,
            "email": email,
            "FechaNacimiento": FechaNacimiento,
            "Contrasenia": Contrasenia
            }
    respuesta = requests.post(f'{rest_api.API_URL}/usuarios', json=body)
    # Al igual que en el caso de la validacion, simplificamos el manejo de errores
    return respuesta.status_code == 200


def obtener_usuarios():
    respuesta = requests.get(f'{rest_api.API_URL}/usuarios')
    return respuesta.json()


def C_inicial(User, N_estudio, A_bien, A_mal):
    body = {"User": User,
            "N_estudio": N_estudio,
            "A_bien": A_bien,
            "A_mal": A_mal
            }
    respuesta = requests.post(f'{rest_api.API_URL}/C_inicial', json=body)
    # Al igual que en el caso de la validacion, simplificamos el manejo de errores
    return respuesta.status_code == 200


def obtener_usuario(IDUsuario):
    respuesta = requests.get(f'{rest_api.API_URL}/usuarios',
                             params={'IDUsuario': IDUsuario})  # acomodar eso del ususario/id (obtener por id)
    return respuesta.json()


def crear_MCF(Cuestion):
    body = {"Cuestion": Cuestion}
    respuesta = requests.post(f'{rest_api.API_URL}/ayudafU', json=body)
    # Al igual que en el caso de la validacion, simplificamos el manejo de errores
    return respuesta.status_code == 200


def obtener_MCF(parecido):
    respuesta = requests.get(f'{rest_api.API_URL}/ayudafU/{parecido}')
    return respuesta.json()


def modificar_user(ID, A_tematicas, Genero, NombreUsuario, email, FechaNacimiento, Contrasenia):
    body = {"A_tematicas": A_tematicas,
            "Genero": Genero,
            "NombreUsuario": NombreUsuario,
            "email": email,
            "FechaNacimiento": FechaNacimiento,
            "Contrasenia": Contrasenia
            }
    respuesta = requests.put(f'{rest_api.API_URL}/usuarios/{ID}', json=body)
    # Al igual que en el caso de la validacion, simplificamos el manejo de errores
    return respuesta.status_code == 200


'''
def C_inicial(User, N_estudio, A_bien, A_mal):
    body = {"User": User,
            "N_estudio": N_estudio,
            "A_bien": A_bien,
            "A_mal": A_mal
            }
    respuesta = requests.post(f'{rest_api.API_URL}/C_inicial', json=body)
    # Al igual que en el caso de la validacion, simplificamos el manejo de errores
    return respuesta.status_code == 200


def obtener_usuario(IDUsuario):
    respuesta = requests.get(f'{rest_api.API_URL}/usuarios', params={'IDUsuario':IDUsuario})#acomodar eso del ususario/id (obtener por id)
    return respuesta.json()
'''


def crear_consulta(ID_UsuarioC, Q, F, P, Liter, Leng, I, M, A, B, O, Consulta):
    body = {"ID_UsuarioC": ID_UsuarioC,
            "Q": Q, "F": F, "P": P, "Liter": Liter, "Leng": Leng, "I": I, "M": M,
            "A": A, "B": B, "O": O,
            "Consulta": Consulta
            }
    respuesta = requests.post(f'{rest_api.API_URL}/consultas', json=body)
    # Al igual que en el caso de la validacion, simplificamos el manejo de errores
    return respuesta.status_code == 200


def obtener_Consultas(parecido, ID_UsuarioC):
    body = {"Consulta": parecido,
            "ID_UsuarioC": ID_UsuarioC
            }
    respuesta = requests.get(f'{rest_api.API_URL}/consultas/particular', json=body)
    return respuesta.json()


def modificar_Consulta(IDc, ID_UsuarioC, Q, F, P, Liter, Leng, I, M, A, B, O, Consulta, Estado):
    body = {"A": A, "B": B, "Consulta": Consulta, "Estado": Estado, "F": F, "I": I, "ID_UsuarioC": ID_UsuarioC,
            "Leng": Leng, "Liter": Liter, "M": M, "O": O, "P": P, "Q": Q
            }
    respuesta = requests.put(f'{rest_api.API_URL}/consultas/{IDc}', json=body)
    # Al igual que en el caso de la validacion, simplificamos el manejo de errores
    return respuesta.status_code == 200


def eliminar_Consulta(IDc):
    respuesta = requests.delete(f'{rest_api.API_URL}/consultas/{IDc}')
    return respuesta.json()


def obtener_AllConsultas():
    respuesta = requests.get(f'{rest_api.API_URL}/consultas')
    return respuesta.json()


def obtener_TutiResp():
    respuesta = requests.get(f'{rest_api.API_URL}/respuestas')
    return respuesta.json()


def crear_comentario(IDc, ID_UsuarioR, Respuesta, Fecha):
    body = {"ID_UsuarioR": ID_UsuarioR,
            "IDc": IDc,
            "Respuesta": Respuesta,
            "Fecha": Fecha
            }
    respuesta = requests.post(f'{rest_api.API_URL}/respuestas', json=body)
    # Al igual que en el caso de la validacion, simplificamos el manejo de errores
    return respuesta.status_code == 200

def obtener_comentarios():
    respuesta = requests.get(f'{rest_api.API_URL}/respuestas')
    return respuesta.json()


def eliminar_Com(ID):
    respuesta = requests.delete(f'{rest_api.API_URL}/respuestas/{ID}')
    return respuesta.json()