import unicodedata
def crear_servicio(datos):
    datos=dict(datos)
    servicio={}
    servicio["nombre"]=input("Ingrese el nombre del servicio: ")
    servicio["tiempo"]= input("Ingrese el tiempo que dura el servicio: ")
    servicio["detalles"]=input("Ingrese los detalles del servicio: ")
    try:
        servicio["precio"] = int(input("Ingrese el precio del servicio: "))
    except Exception:
         servicio["precio"] = 0
    datos["servicios"].append(servicio)
    print("Servicio registrado con éxito!")
    return datos

def leer_servicio(datos):
    datos=dict(datos)
    print("Los servicios que se encuentran en Claro")
    for i in range (len(datos["servicios"])):
           print (datos["servicios"][i])
    return datos       

def actualizar_servicio(datos):
    datos=dict(datos)
    servicio2= input("Ingrese el nombre del servicio que desea actualizar: ")
    dato_cambiar=input("Ingrese el dato que desea cambiar: ")
    nuevo_valor=input("Ingrese el nuevo dato: ")
    for i in range (len(datos["servicios"])):
         if datos["servicios"][i]["nombre"]==servicio2:
            datos["servicios"][i][dato_cambiar]=nuevo_valor
            print(f"La informacion de {servicio2} ha sido actualizada")
    return datos

def eliminar_servicios(datos):
    datos = dict(datos)
    servicio2 = input("Ingrese el nombre del servicio que desea eliminar: ")
    servicio2_normalizado = unicodedata.normalize("NFKD", servicio2).casefold()
    for i, servicio in enumerate(datos["servicios"]):
        nombre_servicio_normalizado = unicodedata.normalize("NFKD", servicio["nombre"]).casefold()
        if nombre_servicio_normalizado == servicio2_normalizado:
            datos["servicios"].pop(i)
            print("Servicio eliminado")
            return datos
    print("El servicio no existe")
    return datos       