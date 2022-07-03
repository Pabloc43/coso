from Datos.base_de_datos import BaseDeDatos


# ADMIN

def obtener_MCFA(IDc):
    obtener_mConsultasF_sql = f''' SELECT * FROM metaDudasF 
                                   WHERE IDc = "{IDc}"
                            '''
    bd = BaseDeDatos()
    return [{
        "IDc": registro[0],
        "Cuestion": registro[1],
        "rCuestion": registro[2]
    } for registro in bd.ejecutar_sql(obtener_mConsultasF_sql)]


def modificar_MCF(IDc, datos_Mconsulta):
    modificar_Consulta_sql = f"""UPDATE metaDudasF SET rCuestion = '{datos_Mconsulta['rCuestion']}'
                                             WHERE IDc = {IDc}
                              """
    bd = BaseDeDatos()
    bd.ejecutar_sql(modificar_Consulta_sql)


def borrar_MconsultaF(IDc):
    obtener_consulta_sql = f"""DELETE FROM metaDudasF
                                     WHERE IDc = {IDc}
                            """
    bd = BaseDeDatos()
    bd.ejecutar_sql(obtener_consulta_sql)


# USER
def obtener_MCFU(parecido):
    obtener_mConsultasF_sql = f''' SELECT * FROM metaDudasF 
                                   WHERE Cuestion LIKE "%{parecido}%"
                            '''
    bd = BaseDeDatos()
    return [{
        "IDc": registro[0],
        "Cuestion": registro[1],
        "rCuestion": registro[2]
    } for registro in bd.ejecutar_sql(obtener_mConsultasF_sql)]


def crear_MCF(Cuestion):
    crear_mConsultaF_sql = f"""INSERT INTO metaDudasF(Cuestion) 
                                            VALUES('{Cuestion}')
                          """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_mConsultaF_sql)



########################################################################################################################