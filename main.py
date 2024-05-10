from datos import *
from menu import *

BASE_DE_DATOS="registro.json"

datos=cargar_datos(BASE_DE_DATOS)

while True:
    menu_principal()
    opc=pedir_opcion()
    if opc==1:
        datos=









    break







guardar_datos(datos, BASE_DE_DATOS)