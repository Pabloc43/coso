from Datos.base_de_datos import BaseDeDatos


#En apariencia poner link hacia personalizacion, con atributos (nota para despues hacerlo)
def obtener_bot(ID_Bot):
    obtener_Bot_sql = f''' SELECT IDBot, Apodo, Apariencia
                                FROM Usuario
                                WHERE IDBot = {ID_Bot}
                            '''
    bd = BaseDeDatos()
    return [{
             "IDBot": registro[0],
             "Apodo": registro[1],
             "Apariencia": registro[2]
             } for registro in bd.ejecutar_sql(obtener_Bot_sql)]


def crear_bot(Apodo, Apariencia):
    crear_Bot_sql = f"""INSERT INTO Bot(
                               Apodo, Apariencia) 
                                 VALUES(
                               '{Apodo}', '{Apariencia}')
                     """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_Bot_sql)


def modificar_bot(ID_Bot, datos_bot):
    modificar_Bot_sql = f"""UPDATE Bot SET Apodo = '{datos_bot['Apodo']}',
                                           Apariencia = '{datos_bot['Apariencia']}'
                                     WHERE IDBot = {ID_Bot}
                             """
    bd = BaseDeDatos()
    bd.ejecutar_sql(modificar_Bot_sql)