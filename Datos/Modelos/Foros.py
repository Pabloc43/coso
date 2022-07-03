from Datos.base_de_datos import BaseDeDatos



def obtener_foro(ID_foro):
    obtener_Foro_sql = f''' SELECT IDf, UsuarioCuestiona, Consulta, UsuarioResponde, Respuesta, Estado
                                FROM Foros
                                WHERE IDf = {ID_foro}
                            '''
    bd = BaseDeDatos()
    return [{
             "IDf": registro[0],
             "UsuarioCuestiona": registro[1],
             "Consulta": registro[2],
             "UsuarioResponde": registro[3],
             "Respuesta": registro[4],
             "Estado": registro[5]
             } for registro in bd.ejecutar_sql(obtener_Foro_sql)]


def obtener_foros():
    obtener_Foros_sql = ''' SELECT IDf, UsuarioCuestiona, Consulta, UsuarioResponde, Respuesta, Estado
                                FROM Foros
                        '''
    bd = BaseDeDatos()
    return [{
             "IDf": registro[0],
             "UsuarioCuestiona": registro[1],
             "Consulta": registro[2],
             "UsuarioResponde": registro[3],
             "Respuesta": registro[4],
             "Estado": registro[5]
             } for registro in bd.ejecutar_sql(obtener_Foros_sql)]


def crear_foro(UsuarioCuestiona, Consulta, UsuarioResponde, Respuesta, Estado):
    crear_foro_sql = f'''INSERT INTO Foros(UsuarioCuestiona, Consulta, UsuarioResponde, Respuesta, Estado)
                                    VALUES('{UsuarioCuestiona}', '{Consulta}', '{UsuarioResponde}', '{Respuesta}', {Estado})
                      '''
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_foro_sql)


