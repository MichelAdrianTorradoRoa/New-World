def crear_servicio(datos):
    datos=dict(datos)
    servicio={}
    servicio["nombre"]=input("Ingrese el nombre del servicio: ")
    servicio["tiempo"]= input("Ingrese el tiempo que dura el servicio: ")
    servicio["detalles"]=input("Ingrese los detalles del servicio: ")
    try:
        servicio["precio"] = float(input("Ingrese el precio del servicio: "))
    except Exception:
         servicio["precio"] = 0
    datos["servicios"].append(servicio)
    print("Servicio registrado con éxito!")
    return datos

