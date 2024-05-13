import unicodedata
import json

def crear_perfiles_usuarios(datos):
    datos=dict(datos)
    usuario={}
    usuario["nombre"]=input("Ingrese el nombre del usuario: ")
    usuario["categoria"]=("Cliente Nuevo")
    usuario["tipo del documento de identidad"]=input("Ingrese el tipo del documento de identidad: ")
    try:
        usuario["numero del documento de identidad"] = int(input("Ingrese el numero de identidad: "))
    except Exception:
          usuario["informacion de contacto"] = 0
    usuario["direccion"]=input("Ingrese la direccion del usuario: ")
    usuario["correo electronico"]=input("Ingrese el correo electronico: ")
    try:
        usuario["informacion de contacto"] = int(input("Ingrese el numero telefonico: "))
    except Exception:
          usuario["informacion de contacto"] = 0
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
    datos=dict(datos)
    nombre2= input("Ingrese el nombre del usuario que desea actualizar: ")
    dato_cambiar=input("Ingrese el dato que desea cambiar: ")
    nuevo_valor=input("Ingrese el nuevo dato: ")
    for i in range (len(datos["usuarios"])):
         if datos["usuarios"][i]["nombre"]==nombre2:
            datos["usuarios"][i][dato_cambiar]=nuevo_valor
            print(f"La informacion de {nombre2} ha sido actualizada")
    return datos

def eliminar_usuarios(datos):
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

def eliminar_usuario(datos):
    datos=dict(datos)
    nombre2= input("Ingrese el nombre del usuario que desea eliminar: ")
    for i in range (len(datos["usuarios"])):
        if datos["usuarios"][i]["nombre"]==nombre2:
            datos["usuarios"].pop(i)
            print("Usuario eliminado")
        return datos
    print("El usuario no existe")
    return datos
     
def cliente_nuevo(datos):
    datos=dict(datos)
    nombre2=input("Ingrese el nombre del cliente que desea asignarlo como cliente nuevo: ")
    for i in range (len(datos["usuarios"]["nombre"])):
        if datos["usuarios"][i]["nombre"]==nombre2:
            if datos["usuarios"][i]["categoria"]=="Cliente Nuevo":
                print("El usuario ya es cliente nuevo")
                return datos
            else:
                datos["usuarios"][i]["categoria"]="Cliente Nuevo"
                print(f"La informacion de {nombre2} ha sido actualizada")
                return datos
        else:
            print("El usuario no exite")
        break
    return datos



