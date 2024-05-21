from datetime import datetime
from errores import *
    
def crear_producto(datos):
    try:
       datos=dict(datos)
       producto = {}
       producto["nombre"] = input("Ingrese el nombre del producto: ")
       producto["marca"] = input("Ingrese la marca del producto: ")
       producto["referencia"] = input("Ingrese la referencia del producto: ")
       producto["cantidad"] = int(input("Ingrese la cantidad disponible: "))
       producto["valor"] = int(input("Ingrese el valor del producto: "))
    except Exception:
        ahora = datetime.datetime.now()
        dato = ahora.strftime("%Y-%m-%d %H:%M:%S")
        mensaje = "Fallo en crear producto"
        guardar_txt(dato, mensaje)

    datos["productos"].append(producto)
    print("Producto registrado exitosamente!")
    return datos

def leer_catalogo_productos(datos):
    datos=dict(datos)
    print("Catálogo de Productos:")
    for i in range (len(datos["productos"])):
        print (datos["productos"][i])
    return datos

def registrar_venta_producto(datos):
    try:
        datos=dict(datos)
        nombre_usuario = input("Ingrese el nombre del usuario que realizó la compra: ")
        nombre_producto = input("Ingrese el nombre del producto vendido: ")
        cantidad = int(input("Ingrese la cantidad vendida: "))
        estado = input("Ingrese el estado de la venta (pendiente, completada, cancelada, etc.): ")
        hora_de_venta = str(datetime.now().replace(microsecond=0))
        
        
        for usuario in datos["usuarios"]:
            if usuario["nombre"] == nombre_usuario:
                for producto in datos["productos"]:
                    if producto["nombre"] == nombre_producto:
                        venta = {
                            "nombre_usuario": nombre_usuario,
                            "nombre_producto": nombre_producto,
                            "cantidad": cantidad,
                            "estado": estado,
                            "hora_de_venta": hora_de_venta
                        }
                    if "ventas" not in producto:
                        producto["ventas"] = []
                        producto["ventas"].append(venta)
                        print("Venta registrada exitosamente")
                        return datos

        print("No se pudo registrar la venta. Verifique el nombre del usuario y del producto.")
        return datos
    except Exception:
        ahora = datetime.datetime.now()
        dato = ahora.strftime("%Y-%m-%d %H:%M:%S")
        mensaje = "Fallo en registrar vental de un producto"
        guardar_txt(dato, mensaje)
        print("valor invalido")

def registrar_venta_servicio(datos):
 try:   
    datos=dict(datos)
    nombre_usuario = input("Ingrese el nombre del usuario que realizó la compra: ")
    nombre_servicio = input("Ingrese el nombre del servicio vendido: ")
    estado = input("Ingrese el estado de la venta (pendiente, completada, cancelada, etc.): ")
    hora_de_venta = str(datetime.now().replace(microsecond=0))

    for usuario in datos["usuarios"]:
        if usuario["nombre"] == nombre_usuario:
            for servicio in datos["servicios"]:
                if servicio["nombre"] == nombre_servicio:
                    venta = {
                        "nombre_usuario": nombre_usuario,
                        "nombre_servicio": nombre_servicio,
                        "estado": estado,
                        "hora_de_venta": hora_de_venta
                    }
                    if "ventas" not in servicio:
                        servicio["ventas"] = []
                        servicio["ventas"].append(venta)
                    print("Venta registrada exitosamente")
                    return datos

    print("No se pudo registrar la venta. Verifique el nombre del usuario y del servicio.")
    return datos
 except Exception:
        ahora = datetime.datetime.now()
        dato = ahora.strftime("%Y-%m-%d %H:%M:%S")
        mensaje = "Fallo en registrar venta de un servicio"
        guardar_txt(dato, mensaje)
        print("valor invalido")

def ver_historial_ventas(datos):  
    datos=dict(datos)
    print("Historial de Ventas:")
    for producto in datos["productos"]:
        if "ventas" in producto:
            print(f"Producto: {producto['nombre']}")
            for venta in producto["ventas"]:
                print(f"Usuario: {venta['nombre_usuario']}, Cantidad: {venta['cantidad']}, Estado: {venta['estado']}")
    for servicio in datos["servicios"]:
        if "ventas" in servicio:
            print(f"Servicio: {servicio['nombre']}")
            for venta in servicio["ventas"]:
                print(f"Usuario: {venta['nombre_usuario']}, Estado: {venta['estado']}")
    return datos