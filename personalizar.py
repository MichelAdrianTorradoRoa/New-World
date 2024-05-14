import unicodedata
import json
def personalizar_servicios(datos):
    datos=dict(datos)
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