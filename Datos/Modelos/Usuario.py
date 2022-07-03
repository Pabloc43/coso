from Datos.base_de_datos import BaseDeDatos


def obtener_usuario(IDUsuario):
    obtener_usuarios_sql = f''' SELECT IDUsuario, A_tematicas, Genero, NombreUsuario,
                                       email, FechaNacimiento, Contrasenia, Rol, IDBot
                                FROM Usuario
                                WHERE IDUsuario = {IDUsuario}
                            '''
    bd = BaseDeDatos()
    return [{
        "IDUsuario": registro[0],
        "A_tematicas": registro[1],
        "Genero": registro[2],
        "NombreUsuario": registro[3],
        "email": registro[4],
        "FechaNacimiento": registro[5],
        "Contrasenia": registro[6],
        "Rol": registro[7],
        "IDBot": registro[8]
    } for registro in bd.ejecutar_sql(obtener_usuarios_sql)]


def obtener_usuarios():
    obtener_usuarios_sql = ''' SELECT IDUsuario, A_tematicas, Genero, NombreUsuario, 
                                       email, FechaNacimiento, Contrasenia, Rol, IDBot
                                FROM Usuario
                           '''
    bd = BaseDeDatos()
    return [{
        "IDUsuario": registro[0],
        "A_tematicas": registro[1],
        "Genero": registro[2],
        "NombreUsuario": registro[3],
        "email": registro[4],
        "FechaNacimiento": registro[5],
        "Contrasenia": registro[6],
        "Rol": registro[7],
        "IDBot": registro[8]
    } for registro in bd.ejecutar_sql(obtener_usuarios_sql)]


def crear_usuario(A_tematicas, Genero, NombreUsuario, email, FechaNacimiento, Contrasenia):
    crear_usuario_sql = f"""INSERT INTO Usuario(
                               A_tematicas, Genero, NombreUsuario, 
                               email, FechaNacimiento, Contrasenia) 
                                        VALUES(
                               '{A_tematicas}', '{Genero}', '{NombreUsuario}',
                               '{email}', '{FechaNacimiento}', '{Contrasenia}')
                         """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_usuario_sql)


def modificar_usuario(IDUsuario, datos_usuario):
    modificar_usuario_sql = f"""UPDATE Usuario SET A_tematicas = '{datos_usuario['A_tematicas']}',
                                                   Genero = '{datos_usuario['Genero']}',
                                                   NombreUsuario = '{datos_usuario['NombreUsuario']}',
                                                   email = '{datos_usuario['email']}',
                                                   FechaNacimiento = '{datos_usuario['FechaNacimiento']}',
                                                   Contrasenia = '{datos_usuario['Contrasenia']}'
                                             WHERE IDUsuario = {IDUsuario}
                             """
    bd = BaseDeDatos()
    bd.ejecutar_sql(modificar_usuario_sql)


def obtener_usuarios_por_NombreUsuario_Contrasenia(NombreUsuario, Contrasenia):
    obtener_usuario_sql = f"""SELECT IDUsuario, NombreUsuario, Rol
                              FROM Usuario
                              WHERE NombreUsuario = '{NombreUsuario}' and Contrasenia = '{Contrasenia}'
                           """
    bd = BaseDeDatos()
    return [{"IDUsuario": registro[0],
             "NombreUsuario": registro[1],
             "Rol": registro[2]
             } for registro in bd.ejecutar_sql(obtener_usuario_sql)]


def borrar_usuario(IDUsuario):
    obtener_usuarios_sql = f"""DELETE FROM Usuario
                                     WHERE IDUsuario = {IDUsuario}
                            """
    bd = BaseDeDatos()
    bd.ejecutar_sql(obtener_usuarios_sql)


def crear_sesion(ID_Usuario, dt_string):
    crear_sesion_sql = f"""INSERT INTO Sesiones(ID_Usuario, FECHA_HORA)
                                         VALUES('{ID_Usuario}', '{dt_string}')
                        """
    bd = BaseDeDatos()
    return bd.ejecutar_sql(crear_sesion_sql, True)


def obtener_sesion(id_sesion):
    obtener_sesion_sql = f"""SELECT ID, ID_Usuario, FECHA_HORA
                               FROM Sesiones
                              WHERE ID = {id_sesion}
                          """
    bd = BaseDeDatos()
    return [{"ID": registro[0],
             "ID_Usuario": registro[1],
             "FECHA_HORA": registro[2]
             } for registro in bd.ejecutar_sql(obtener_sesion_sql)]


def C_inicial(User, N_estudio, A_bien, A_mal):
    C_inicial = f"""INSERT INTO C_inicial(
                               User, N_estudio, A_bien, A_mal) 
                                        VALUES(
                               '{User}', '{N_estudio}', '{A_bien}', '{A_mal}')
                         """
    bd = BaseDeDatos()
    bd.ejecutar_sql(C_inicial)