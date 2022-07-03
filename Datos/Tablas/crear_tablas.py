import sqlite3


sql_tabla_metaDudasf = '''DROP TABLE metaDudasF'''
sql_tabla_metaDudasF = '''CREATE TABLE metaDudasF(
                            IDc integer PRIMARY KEY,
                            Cuestion text NOT NULL,
                            rCuestion text DEFAULT "Gracias por realizar la consulta, responderemos a la brevedad"
                                              )
                     '''
sql_tabla_metaDudasd = '''DROP TABLE metaDudasD'''
sql_tabla_metaDudasD = '''CREATE TABLE metaDudasD(
                            IDc integer PRIMARY KEY,
                            ID_UsuarioC text REFERENCES  Usuario (NombreUsuario),
                            Cuestion text NOT NULL,
                            Estado integer DEFAULT 0,
                            rCuestion
                                              )
                     '''

sql_tabla_C_inicial = '''CREATE TABLE C_inicial(
                                     User text REFERENCES Usuario (NombreUsuario), 
                                     N_estudio text NOT NULL,
                                     A_bien text, 
                                     A_mal text)
                              '''

sql_tabla_Consultas = '''DROP TABLE Consultas'''
sql_tabla_Consulta = '''CREATE TABLE Consultas(
                            IDc integer PRIMARY KEY,
                            ID_UsuarioC text REFERENCES  Usuario (NombreUsuario),
                            Q integer DEFAULT 0, F integer DEFAULT 0, P integer DEFAULT 0,
                            Liter integer DEFAULT 0, Leng integer DEFAULT 0,I integer DEFAULT 0,
                            M integer DEFAULT 0, A integer DEFAULT 0, B integer DEFAULT 0, 
                            O integer DEFAULT 0,
                            Consulta text NOT NULL,
                            Estado integer DEFAULT 0
                                              )
                     '''
sql_tabla_Respuestas = '''DROP TABLE Respuestas'''
sql_tabla_Respuesta = '''CREATE TABLE Respuestas(
                            ID integer PRIMARY KEY,
                            IDc integer REFERENCES Consultas (IDc),
                            ID_UsuarioR text REFERENCES  Usuario (NombreUsuario),
                            Respuesta text NOT NULL,
                            Fecha text NOT NULL
                                              )
                     '''

sql_tabla_Foros = '''CREATE TABLE Foros(
                         IDf integer PRIMARY KEY,
                         UsuarioCuestiona text REFERENCES Usuario(NombreUsuario),
                         Consulta text REFERENCES Consultas (Consulta), 
                         UsuarioResponde text REFERENCES Usuario(NombreUsuario),
                         Respuesta text REFERENCES Respuestas (Respuesta), 
                         Estado integer REFERENCES Consultas (Estado)
                                        )
                  '''

sql_tabla_Bot = '''CREATE TABLE Bot(
                       IDBot integer PRIMARY KEY AUTOINCREMENT, 
                       Apodo text NOT NULL, 
                       Apariencia text NOT NULL
                                    )
                '''

sql_tabla_Usuarios = '''CREATE TABLE Usuario(
                                     IDUsuario integer PRIMARY KEY AUTOINCREMENT, 
                                     A_tematicas text NOT NULL, 
                                     Genero text NOT NULL, 
                                     NombreUsuario text UNIQUE,
                                     email text UNIQUE,
                                     FechaNacimiento text NOT NULL, 
                                     Contrasenia text NOT NULL,
                                     Rol text DEFAULT "usuario",
                                     IDBot integer REFERENCES Bot (IDBot)
                                             )
                              '''
sql_tabla_Sesion = '''CREATE TABLE Sesiones(
                            ID integer PRIMARY KEY,
                            ID_Usuario text REFERENCES  Usuario (NombreUsuario),
                            FECHA_HORA text
                                            )
                     '''

if __name__ == '__main__':
    try:
        print('Creando Base de datos..')
        conexion = sqlite3.connect('../../BaseProyecto.db')

        print('Creando Tablas..')
        #conexion.execute(sql_tabla_metaDudasf)
        #conexion.execute(sql_tabla_metaDudasd)
        #conexion.execute(sql_tabla_metaDudasF)
        #conexion.execute(sql_tabla_metaDudasD)
        #conexion.execute(sql_tabla_C_inicial)
        #conexion.execute(sql_tabla_Consultas)
        #conexion.execute(sql_tabla_Consulta)
        conexion.execute(sql_tabla_Respuestas)
        conexion.execute(sql_tabla_Respuesta)
       # conexion.execute(sql_tabla_Foros)
       # conexion.execute(sql_tabla_Bot)
       # conexion.execute(sql_tabla_Usuarios)
     #   conexion.execute(sql_tabla_Sesion)

        conexion.commit()
        conexion.close()
        print('Creacion Finalizada.')
    except Exception as e:
        print(f'Error creando base de datos: {e}', e)

