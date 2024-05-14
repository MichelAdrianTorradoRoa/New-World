import unicodedata
import json
import datetime
def manejar_excepcion(excepcion):
    echa_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("errores.txt", "a") as archivo_errores:
        archivo_errores.write(f"{fecha_actual}: {excepcion}\n")
    print("Se ha producido un error. Consulte el archivo de errores para más detalles.")
def personalizar_servicios(datos):
    datos=dict(datos)
    try:
        nombre_usuario = input("Ingrese el nombre del usuario: ")
        tipo_interaccion = input("Ingrese el tipo de interacción : ")
        detalle_interaccion = input("Ingrese detalles adicionales sobre la interacción : ")

        servicios_personalizados = []
        for usuario in datos["usuarios"]:
            if usuario["nombre"] == nombre_usuario:
                print("Información del Usuario:")
                print("Nombre:", usuario["nombre"])
                print("Categoría:", usuario["categoria"])
                print("Historial de Compras:", usuario.get("historial_uso_servicio", []))
                print("Interacciones Pasadas:", usuario.get("interacciones", []))
                historial_compras = len(usuario.get("historial_uso_servicio", []))
                print(f"La frecuencia de compras para {nombre_usuario} es: {historial_compras}")
                for servicio in datos["servicios"]:
                    servicios_personalizados.append(servicio["nombre"])
                if tipo_interaccion and detalle_interaccion:
                        if "interacciones" not in usuario:
                            usuario["interacciones"] = []
                        usuario["interacciones"].append({
                             "tipo": tipo_interaccion,
                             "detalle": detalle_interaccion
                        })
                        print(f"Interacción registrada exitosamente para '{nombre_usuario}'")
                if "servicios_personalizados" not in usuario:
                     usuario["servicios_personalizados"] = []
                usuario["servicios_personalizados"].extend(servicios_personalizados)
                return datos
        print("El usuario no fue encontrado.")
        return datos
    except Exception as e:
        manejar_excepcion(e)
        return datos