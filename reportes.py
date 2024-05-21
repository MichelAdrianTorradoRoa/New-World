import datetime
from errores import *
def generar_informe_servicios_populares(datos):
    try:
        datos=dict(datos)
        servicios_populares = {}
        for servicio in datos["servicios"]:
            nombre_servicio = servicio["nombre"]
            cantidad_ventas = len(servicio.get("ventas", []))
            servicios_populares[nombre_servicio] = cantidad_ventas

        servicios_populares_ordenados = sorted(servicios_populares.items(), key=lambda x: x[1], reverse=True)
        print("Servicios más populares:")
        for servicio, cantidad in servicios_populares_ordenados:
            print(f"{servicio}: {cantidad} ventas")
        return datos
    except Exception:
        ahora = datetime.datetime.now()
        dato = ahora.strftime("%Y-%m-%d %H:%M:%S")
        mensaje = "Fallo en reportes"
        guardar_txt(dato, mensaje)
        print("valor invalido")
   