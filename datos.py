import datetime
import json
def manejar_excepcion(excepcion):
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("errores.txt", "a") as archivo_errores:
        archivo_errores.write(f"{fecha_actual}: {excepcion}\n")
    print("Se ha producido un error. Consulte el archivo de errores para más detalles.")

def cargar_datos(archivo):
    datos = {}
    try:
        with open(archivo,"r") as file:
            datos=json.load(file)
        return datos
    except Exception as e:
        manejar_excepcion(e)
        return {}    
        

def guardar_datos(datos, archivo):
    datos = dict(datos)
    try:
        diccionario=json.dumps(datos, indent=4)
        file=open(archivo,"w")
        file.write(diccionario)
        file.close()
    except Exception as e:
        manejar_excepcion(e)
