def crear_perfiles_usuarios(datos):
    datos=dict(datos)
    usuario={}
    usuario["nombre"]=input("Ingrese el nombre del usuario: ")
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
    for i in range (len(datos["usuarios"])):
        if (datos["usuarios"][i]["nombre"])==nombre2:
              dato_cambiar=input("Ingrese el dato que desea cambiar: ")
              print (len(datos["usuarios"]))   

def eliminar_usuarios(datos):
    datos=dict(datos)
    nombre2= input("Ingrese el nombre del usuario que desea eliminar: ")
    for i in range (len(datos["usuarios"])):
        if datos["usuarios"][i]["nombre"]==nombre2:
            datos["usuarios"].pop(i)
            print("Usuario eliminado")
        return datos
    print("El usuario no existe")
    return datos
     