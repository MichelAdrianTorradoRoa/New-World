import datetime
import json
from errores import *
def cargar_datos(archivo):
    datos = {}
    try:
        with open(archivo,"r") as file:
            datos=json.load(file)
        return datos
    except Exception:
        ahora = datetime.datetime.now()
        dato = ahora.strftime("%Y-%m-%d %H:%M:%S")
        mensaje = "Fallo en datos"
        guardar_txt(dato, mensaje)
        print("valor incorrecto")
        return {}    

def guardar_datos(datos, archivo):
    datos = dict(datos)
    try:
        diccionario=json.dumps(datos, indent=4)
        file=open(archivo,"w")
        file.write(diccionario)
        file.close()
    except Exception:
        ahora = datetime.datetime.now()
        dato = ahora.strftime("%Y-%m-%d %H:%M:%S")
        mensaje = "Fallo en datos"
        guardar_txt(dato, mensaje)
        print("valor incorrecto")
    