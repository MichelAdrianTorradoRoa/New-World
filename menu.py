import json
import datos
import datetime
from errores import *

def menu_principal():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Bienvenido al menu de registro y seguimiento de Claro")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("El Módulo de Usuarios (Administrador) contiene las siguientes opciones: ")
    print("1. Registro y Gestión de Usuarios y de Servicios")
    print("2. Seguimiento del Historial de Usuarios")
    print("3. Personalización de Servicios")
    print("4. Gestión de las Ventas")
    print("5. Reportes")
    print("6. Salir")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    
def menu_Registro_y_Gestión_de_Usuarios():
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("En este menu se podra hacer las operaciones CRUD y de asignar categorias a los usuarios")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1. Crear perfiles de usuarios")
        print("2. Leer los perfiles de los usuarios")
        print("3. Actualizar los perfiles de los usuarios")
        print("4. Eliminar perfiles de usuarios")
        print("5. Asignar categorias a los usuarios")
        print("6. Crear un servicio")
        print("7. Leer los servicios ofrecidos")
        print("8. Actualizar los servicios ofrecidos")
        print("9. Eliminar un servicio ofrecido")
        print("10. Salir")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def menu_Asignar_categorias_a_los_usuarios():
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Aqui podras asginarles la respectiva categoria que pertenece cada usuario")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1. Cliente nuevo")
        print("2. Cliente regular")
        print("3. Cliente fiel")
        print("4. Salir")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def menu_Seguimiento_del_Historial_de_Usuarios():
       print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
       print("1. Registro y Almacenamiento de servicios utilizados por cada usuario")
       print("2. Seguimiento de las interacciones de los usuarios con la empresa")
       print("3. Salir")
       print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def menu_Gestión_de_las_Ventas():
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("1. Crear de Productos")
      print("2. Leer Catalogo de Productos")
      print("3. Registrar la Venta del Producto")
      print("4. Registrar la Venta del Servicio")
      print("5. Historial de Ventas")
      print("6. Salir")
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   
    
def pedir_opcion():
    opc = 0
    try:
        opc = int(input("Ingrese su opción: "))
        print("***************************************")
        return opc
    except Exception:
        ahora = datetime.datetime.now()
        dato = ahora.strftime("%Y-%m-%d %H:%M:%S")
        mensaje = "Fallo en menu"
        guardar_txt(dato, mensaje)
        print("--"*20)
        print("valor invalido")
    


