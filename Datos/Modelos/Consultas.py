from Datos.base_de_datos import BaseDeDatos


def obtener_consulta(parecido, ID_UsuarioC):
    obtener_Consulta_sql = f''' SELECT * FROM Consultas WHERE Consulta LIKE "%{parecido}%" AND ID_UsuarioC = "{ID_UsuarioC}"'''
    bd = BaseDeDatos()
    return [{
        "IDc": registro[0],
        "ID_UsuarioC": registro[1],
        "Q": registro[2], "F": registro[3], "P": registro[4], "Liter": registro[5], "Leng": registro[6],
        "I": registro[7], "M": registro[8], "A": registro[9], "B": registro[10], "O": registro[11],
        "Consulta": registro[12],
        "Estado": registro[13]
    } for registro in bd.ejecutar_sql(obtener_Consulta_sql)]


def obtener_consultas():
    obtener_Consultas_sql = ''' SELECT * FROM Consultas'''
    bd = BaseDeDatos()
    return [{
        "IDc": registro[0],
        "ID_UsuarioC": registro[1],
        "Q": registro[2], "F": registro[3], "P": registro[4], "Liter": registro[5], "Leng": registro[6],
        "I": registro[7], "M": registro[8], "A": registro[9], "B": registro[10], "O": registro[11],
        "Consulta": registro[12],
        "Estado": registro[13]
    } for registro in bd.ejecutar_sql(obtener_Consultas_sql)]


def crear_consulta(ID_UsuarioC, Q, F, P, Liter, Leng, I, M, A, B, O, Consulta):
    crear_Consulta_sql = f"""INSERT INTO Consultas(ID_UsuarioC, Q, F, P, Liter, Leng, I, M, A, B, O, Consulta) 
                                            VALUES('{ID_UsuarioC}', {Q}, {F}, {P}, {Liter}, {Leng}, {I}, 
                                                   {M}, {A}, {B}, {O}, '{Consulta}'
                                                   )
                          """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_Consulta_sql)


def modificar_consulta(IDConsulta, datos_consulta):
    modificar_Consulta_sql = f"""UPDATE Consultas SET Q = {datos_consulta['Q']}, F = {datos_consulta['F']},
                                                      P = {datos_consulta['P']}, Liter = {datos_consulta['Liter']}, 
                                                      Leng = {datos_consulta['Leng']}, I = {datos_consulta['I']}, 
                                                      M = {datos_consulta['M']}, A = {datos_consulta['A']}, 
                                                      B = {datos_consulta['B']}, O = {datos_consulta['O']},
                                                      Consulta = '{datos_consulta['Consulta']}',
                                                      Estado = {datos_consulta['Estado']}
                                             WHERE IDc = {IDConsulta}
                              """
    bd = BaseDeDatos()
    bd.ejecutar_sql(modificar_Consulta_sql)


def borrar_consulta(IDConsulta):
    obtener_consulta_sql = f"""DELETE FROM Consultas
                                     WHERE IDc = {IDConsulta}
                            """
    bd = BaseDeDatos()
    bd.ejecutar_sql(obtener_consulta_sql)


