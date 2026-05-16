# -------------------------------------------------------------------------
# Se importan los modulos requeridos, algunos completos, y uno con alias
# -------------------------------------------------------------------------

from clase import Participante
import csv, json, re
import datetime as dt

#------------------------------------------------------
#   Función para válidar un numero entero (Jesus)
#------------------------------------------------------

def get_int(s:str):

    while True:
        num = input(f"{s}: ")
        try:
            num = int(num)
            return num
    
        except ValueError:
            if num == "X" or num == "x":
                num = str(num)
                return num
            print("Debe ingresar un numero entero")
