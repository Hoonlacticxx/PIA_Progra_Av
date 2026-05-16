import funciones as fun

# --------------------------------------------------------------------------
# Modulo que ejecuta las funciones en base a una funcion de menu (Arturo)
# --------------------------------------------------------------------------

participantes = list()
info = fun.cargar_info(participantes)

while True:
    home = fun.menu()
    if home == 1:
        x = fun.cargar_info(participantes)
    elif home == 2:
        x = fun.registrar_participante(participantes)
    elif home == 3:
        x = fun.buscar_participante(participantes)
    elif home == 4:
        x = fun.mod_participante(participantes)
    elif home == 5:
        x = fun.del_participante(participantes)
    elif home == 6:
        fun.lista_participantes(participantes)
    elif home == 7:
        x = fun.upd_info(participantes)
    elif home == 8:
        x = fun.serializar(participantes)
        print("")
        print(x)
    elif home == "X" or home == "x":
        break
    else:
        print("Opción no valida")