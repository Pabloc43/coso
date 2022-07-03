from Datos.base_de_datos import BaseDeDatos


def responder_consulta(IDc, ID_UsuarioR, Respuesta, fecha):
    crear_Respuesta_sql = f"""INSERT INTO Respuestas(IDc, ID_UsuarioR, Respuesta, Fecha) 
                                            VALUES({IDc}, '{ID_UsuarioR}', '{Respuesta}', '{fecha}'
                                                    )
                          """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_Respuesta_sql)


def borrar_respuesta(ID):
    borrar_Respuesta_sql = f"""DELETE FROM Respuestas
                                     WHERE ID = {ID}
                            """
    bd = BaseDeDatos()
    bd.ejecutar_sql(borrar_Respuesta_sql)


def modificar_respuesta(ID, datos_respuesta):
    modificar_Respuesta_sql = f"""UPDATE Respuestas SET Respuesta = '{datos_respuesta['Respuesta']}'
                                             WHERE ID = {ID}
                             """
    bd = BaseDeDatos()
    bd.ejecutar_sql(modificar_Respuesta_sql)


def obtener_respuestas():
    obtener_resp_sql = f''' SELECT * FROM Respuestas'''
    bd = BaseDeDatos()

    return [{
        "ID": registro[0],
        "IDc": registro[1],
        "ID_UsuarioR": registro[2],
        "Respuesta": registro[3],
        "Fecha": registro[4]
    } for registro in bd.ejecutar_sql(obtener_resp_sql)]
