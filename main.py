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