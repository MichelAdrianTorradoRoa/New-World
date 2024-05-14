import datetime
def manejar_excepcion(excepcion):
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("errores.txt", "a") as archivo_errores:
        archivo_errores.write(f"{fecha_actual}: {excepcion}\n")
    print("Se ha producido un error. Consulte el archivo de errores para más detalles.")
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
    except Exception as e:
        manejar_excepcion(e)
        return datos