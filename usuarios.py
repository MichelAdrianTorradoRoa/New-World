import unicodedata
import json
import datetime
from errores import *
def crear_perfiles_usuarios(datos):
    datos=dict(datos)
    usuario={}
    usuario["nombre"]=input("Ingrese el nombre del usuario: ")
    usuario["categoria"]=("Cliente Nuevo")
    usuario["tipo del documento de identidad"]=input("Ingrese el tipo del documento de identidad: ")
    try:
       usuario["numero del documento de identidad"] = int(input("Ingrese el numero de identidad: "))
    except Exception:
        usuario["numero del documento de identidad"] = 0
        ahora = datetime.datetime.now()
        dato = ahora.strftime("%Y-%m-%d %H:%M:%S")
        mensaje = "Fallo en crear usuario(numero ID)"
        guardar_txt(dato, mensaje)
        print("valor invalido")

    usuario["direccion"]=input("Ingrese la direccion del usuario: ")
    usuario["correo electronico"]=input("Ingrese el correo electronico: ")
    try:
        usuario["informacion de contacto"] = int(input("Ingrese el numero telefonico: "))
    except Exception:
        usuario["informacion de contacto"] = 0
        ahora = datetime.datetime.now()
        dato = ahora.strftime("%Y-%m-%d %H:%M:%S")
        mensaje = "Fallo en crear usuario"
        guardar_txt(dato, mensaje)
        print("valor invalido")
        m="Valor invalido"
        if m=="Fallo en crear usuario":
            print("Revisar")
            return datos
        else:
            usuario["historial_uso_servicio"] = []      
            datos["usuarios"].append(usuario)
            print("Usuario registrado con éxito!")
            return datos


def leer_usuarios(datos):
    datos=dict(datos)
    print("Los usuarios que se encuentran en Claro")
    for i in range (len(datos["usuarios"])):
           print (datos["usuarios"][i])
    return datos       
    
def actualizar_usarios(datos):
    try:
      datos=dict(datos)
      nombre2= input("Ingrese el nombre del usuario que desea actualizar: ")
      dato_cambiar=input("Ingrese el dato que desea cambiar: ")
      nuevo_valor=input("Ingrese el nuevo dato: ")
      for i in range (len(datos["usuarios"])):
          if datos["usuarios"][i]["nombre"]==nombre2:
            datos["usuarios"][i][dato_cambiar]=nuevo_valor
            print(f"La informacion de {nombre2} ha sido actualizada")
      return datos
    except Exception:
        ahora = datetime.datetime.now()
        dato = ahora.strftime("%Y-%m-%d %H:%M:%S")
        mensaje = "Fallo en actualizar usuario"
        guardar_txt(dato, mensaje)
        print("valor invalido")

def eliminar_usuarios(datos):
    try:
       datos = dict(datos)
       nombre2 = input("Ingrese el nombre del usuario que desea eliminar: ")
       # Normalizar el nombre ingresado
       nombre2_normalizado = unicodedata.normalize("NFKD", nombre2).casefold()
       for i, usuario in enumerate(datos["usuarios"]):
        # Normalizar el nombre del usuario en la lista
        nombre_usuario_normalizado = unicodedata.normalize("NFKD", usuario["nombre"]).casefold()
        if nombre_usuario_normalizado == nombre2_normalizado:
            datos["usuarios"].pop(i)
            print("Usuario eliminado")
            return datos
        print("El usuario no existe")
        return datos
    except Exception:
        ahora = datetime.datetime.now()
        dato = ahora.strftime("%Y-%m-%d %H:%M:%S")
        mensaje = "Fallo en eliminar usuario"
        guardar_txt(dato, mensaje)
        print("valor invalido")           

def cliente_nuevo(datos):
    try:
       datos=dict(datos)
       nombre2=input("Ingrese el nombre del usuario que desea asignarlo como cliente nuevo: ")
       for i in range (len(datos["usuarios"])):
           if datos["usuarios"][i]["nombre"]==nombre2:
               if datos["usuarios"][i]["categoria"]=="Cliente Nuevo":
                print("El usuario ya es cliente nuevo")
                return datos
               else:
                datos["usuarios"][i]["categoria"]="Cliente Nuevo"
                print(f"La informacion de {nombre2} ha sido actualizada")
                return datos
           return datos
    except Exception:
        ahora = datetime.datetime.now()
        dato = ahora.strftime("%Y-%m-%d %H:%M:%S")
        mensaje = "Fallo en asignarlo como cliente nuevo"
        guardar_txt(dato, mensaje)
        print("valor invalido")   

def cliente_regular(datos):
    try:
        datos=dict(datos)
        nombre2=input("Ingrese el nombre del usuario que desea asignarlo como cliente regular: ")
        for i in range (len(datos["usuarios"])):
            if datos["usuarios"][i]["nombre"]==nombre2:
                if datos["usuarios"][i]["categoria"]=="Cliente Regular":
                    print("El usuario ya es cliente regular")
                    return datos
                else:
                    datos["usuarios"][i]["categoria"]="Cliente Regular"
                    print(f"La informacion de {nombre2} ha sido actualizada")
                    return datos
            return datos
    except Exception:
        ahora = datetime.datetime.now()
        dato = ahora.strftime("%Y-%m-%d %H:%M:%S")
        mensaje = "Fallo en asignarlo como cliente regular"
        guardar_txt(dato, mensaje)
        print("valor invalido")

def cliente_fiel(datos):
    try:
        datos=dict(datos)
        nombre2=input("Ingrese el nombre del usuario que desea asignarlo como cliente fiel: ")
        for i in range (len(datos["usuarios"])):
            if datos["usuarios"][i]["nombre"]==nombre2:
                if datos["usuarios"][i]["categoria"]=="Cliente Fiel":
                    print("El usuario ya es cliente fiel")
                    return datos
                else:
                    datos["usuarios"][i]["categoria"]="Cliente Fiel"
                    print(f"La informacion de {nombre2} ha sido actualizada")
                    return datos
            return datos
    except Exception:
        ahora = datetime.datetime.now()
        dato = ahora.strftime("%Y-%m-%d %H:%M:%S")
        mensaje = "Fallo en asignarlo como cliente fiel"
        guardar_txt(dato, mensaje)
        print("valor invalido")    

def asignar_servicio_a_usuario(datos):
 try:
    nombre_usuario = input("Ingrese el nombre del usuario al que desea asignar el servicio: ")
    nombre_servicio = input("Ingrese el nombre del servicio que desea asignar: ")
    fecha_servicio = input("Ingrese la fecha en que se utilizó el servicio (opcional): ")

    for usuario in datos["usuarios"]:
        if usuario["nombre"] == nombre_usuario:
            for servicio in datos["servicios"]:
                if servicio["nombre"] == nombre_servicio:
                    if "historial_uso_servicio" not in usuario:
                        usuario["historial_uso_servicio"] = []
                    usuario["historial_uso_servicio"].append({
                        "nombre": nombre_servicio,
                        "fecha": fecha_servicio if fecha_servicio else "No especificada"
                    })
                    print(f"Servicio '{nombre_servicio}' asignado correctamente a '{nombre_usuario}'")
                    return datos
            print(f"El servicio '{nombre_servicio}' no existe")
            return datos
    print(f"El usuario '{nombre_usuario}' no existe")
    return datos
 except Exception:
        ahora = datetime.datetime.now()
        dato = ahora.strftime("%Y-%m-%d %H:%M:%S")
        mensaje = "Fallo en asignar servicio a usuario"
        guardar_txt(dato, mensaje)
        print("valor invalido")

def registrar_interaccion_usuario(datos):
 try:   
    nombre_usuario = input("Ingrese el nombre del usuario con quien se realizó la interacción: ")
    tipo_interaccion = input("Ingrese el tipo de interacción (consulta, reclamación, sugerencia, etc.): ")
    detalle_interaccion = input("Ingrese detalles adicionales sobre la interacción: ")

    for usuario in datos["usuarios"]:
        if usuario["nombre"] == nombre_usuario:
            if "interacciones" not in usuario:
                usuario["interacciones"] = []
            usuario["interacciones"].append({
                "tipo": tipo_interaccion,
                "detalle": detalle_interaccion
            })
            print(f"Interacción registrada exitosamente para '{nombre_usuario}'")
            return datos

    print(f"No se encontró ningún usuario con el nombre '{nombre_usuario}'")
    return datos
 except Exception:
        ahora = datetime.datetime.now()
        dato = ahora.strftime("%Y-%m-%d %H:%M:%S")
        mensaje = "Fallo en registrar la interraccion del usuario"
        guardar_txt(dato, mensaje)
        print("valor invalido")