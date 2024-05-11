from datos import *
from menu import *
from usuarios import *

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
            elif opc == 10:
                print("Salió!!")
                break
    
        
            
    elif opc==2:
        while True:
            menu_Seguimiento_del_Historial_de_Usuarios()
            opc=pedir_opcion()
            if opc==1:
                datos=crear_perfiles_usuarios(datos)
            elif opc == 3:
                print("Salió!!")
                break
    




    elif opc==4:
        while True:
            menu_Gestión_de_las_Ventas()
            opc=pedir_opcion()
            if opc==1:
                datos=crear_perfiles_usuarios(datos)
            elif opc == 3:
                print("Salió!!")
                break
    


    
    
    
    
    
    
    
    
    
    elif opc == 6:
        print("Salió!!")
    break








guardar_datos(datos, BASE_DE_DATOS)