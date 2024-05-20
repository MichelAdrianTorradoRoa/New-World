from datetime import datetime
def manejar_excepcion(excepcion):
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("errores.txt", "a") as archivo_errores:
        archivo_errores.write(f"{fecha_actual}: {excepcion}\n")
    print("Se ha producido un error. Consulte el archivo de errores para más detalles.")
    
def crear_producto(datos):
    datos=dict(datos)
    producto = {}
    producto["nombre"] = input("Ingrese el nombre del producto: ")
    producto["marca"] = input("Ingrese la marca del producto: ")
    producto["referencia"] = input("Ingrese la referencia del producto: ")
    producto["cantidad"] = int(input("Ingrese la cantidad disponible: "))
    producto["valor"] = float(input("Ingrese el valor del producto: "))

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

def registrar_venta_servicio(datos):
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