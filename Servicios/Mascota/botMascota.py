from Datos.Modelos import Bot as modelo_bot



def obtener_bot(ID_Bot):
    Bot = modelo_bot.obtener_bot(ID_Bot)
    if len(Bot) == 0:
        raise Exception('No existe tal Bot')
    return Bot[0]


def crear_bot(Apodo, Apariencia):
    modelo_bot.crear_bot(Apodo, Apariencia)


def modificar_bot(ID_Bot, datos_bot):
    modelo_bot.modificar_bot(ID_Bot, datos_bot)