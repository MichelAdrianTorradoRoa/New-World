def crear_perfiles_usuarios(datos):
    datos=dict(datos)
    usuario={}
    usuario["nombre"]=input("Ingrese el nombre del usuario")
    usuario["direccion"]=input("Ingrese la direccion del usuario")
    try:
        usuario["informacion de contacto"] = int(input("Ingrese el numero telefonico: "))
    except Exception:
          usuario["informacion de contacto"] = 0
    opc = -1
    
