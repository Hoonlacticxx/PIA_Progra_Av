#------------------------------------------------------
#   Función que muestra el menú de acciones (Arturo)
#------------------------------------------------------

def menu() -> int:

    while True:
        print("""
----- Seleccione una opción -----
[1] Cargar informacion de CSV
[2] Registrar participantes
[3] Buscar participante
[4] Modificar participante
[5] Eliminar participante
[6] Ver lista de participantes
[7] Actualizar información de CSV
[8] Serializar información a JSON
[X] Terminar y salir
----------------------------------
""")
        num = get_int("Opción")
        if num == "X" or num == "x":
            return num
        elif 0 < num < 9:
            return num
        print("Opción no válida")
        
# --------------------------------------------------------------------------
# Modulo que ejecuta las funciones en base a una funcion de menu (Arturo)
# --------------------------------------------------------------------------

from funciones import *

participantes = list()
info = cargar_info(participantes)

while True:
    home = menu()
    if home == 1:
        x = cargar_info(participantes)
    elif home == 2:
        x = registrar_participante(participantes)
    elif home == 3:
        x = buscar_participante(participantes)
    elif home == 4:
        x = mod_participante(participantes)
    elif home == 5:
        x = del_participante(participantes)
    elif home == 6:
        lista_participantes(participantes)
    elif home == 7:
        x = upd_info(participantes)
    elif home == 8:
        x = serializar(participantes)
        print("")
        print(x)
    elif home == "X" or home == "x":
        break
    else:
        print("Opción no valida")