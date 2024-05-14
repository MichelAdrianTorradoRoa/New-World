from datos import *
from menu import *
from usuarios import *
from servicios import *
from ventas import *
from reportes import *
from personalizar import *
import unicodedata

BASE_DE_DATOS="registro.json"

datos=cargar_datos(BASE_DE_DATOS)

while True:
    menu_principal()
    opc=pedir_opcion()
    if opc==1:
        while True:
            menu_Registro_y_Gestión_de_Usuarios()
            opc=pedir_opcion()
            if opc==1:
                datos=crear_perfiles_usuarios(datos)
            elif opc==2:
                datos=leer_usuarios(datos)
            elif opc==3:
                datos=actualizar_usarios(datos)
            elif opc==4:
                datos=eliminar_usuarios(datos)
            elif opc==5:
                while True:
                    menu_Asignar_categorias_a_los_usuarios()
                    opc=pedir_opcion()
                    if opc==1:
                        datos=cliente_nuevo(datos)
                    elif opc==2:
                        datos=cliente_regular(datos)
                    elif opc==3:
                        datos=cliente_fiel(datos)         
                    elif opc==4:
                        print("Salió!!")
                    break
            elif opc==6:
                datos=crear_servicio(datos)
            elif opc==7:
                datos=leer_servicio(datos)
            elif opc==8:
                datos=actualizar_servicio(datos)
            elif opc==9:
                datos=eliminar_servicios(datos)
            elif opc == 10:
                print("Salió!!")
            break
            
    elif opc==2:
        while True:
            menu_Seguimiento_del_Historial_de_Usuarios()
            opc=pedir_opcion()
            if opc==1:
                datos=asignar_servicio_a_usuario(datos)
            elif opc==2:
                datos=registrar_interaccion_usuario(datos)   
            elif opc == 3:
                print("Salió!!")
            break
    elif opc==3:
        datos=personalizar_servicios(datos)
    elif opc==4:
        while True:
            menu_Gestión_de_las_Ventas()
            opcion = pedir_opcion()
            if opcion == 1:
                crear_producto(datos)
            elif opcion == 2:
                leer_catalogo_productos(datos)
            elif opcion == 3:
                registrar_venta_producto(datos)
            elif opcion == 4:
                registrar_venta_servicio(datos)
            elif opcion == 5:
                ver_historial_ventas(datos)
            elif opcion == 6:
                print("Salio!!")
            break
    elif opc==5:
        datos=generar_informe_servicios_populares(datos)
    elif opc == 6:
        print("Salió!!")
    break

guardar_datos(datos, BASE_DE_DATOS)