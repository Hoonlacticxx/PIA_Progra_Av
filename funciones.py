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
#------------------------------------------------------
#   Función para válidar el nombre de los participantes (Amaniel)
#------------------------------------------------------

def get_nombre() -> str:

    while True:
        nombre = input("Nombre completo: ")
        if re.match(r"^[aA-zZ áÁéÉíÍóÓúÚñÑ]{3,50}$", nombre):
            return nombre
        print("Nombre no válido")

#-------------------------------------------------------------------------------------
#   Función para validar una fecha en formato dd-mm-aaaa. En bucle hasta recibirla (Amaniel)
#-------------------------------------------------------------------------------------

def get_fecha(s: str) -> str:
   
   while True:
      fecha = input(f"Ingrese {s} en formato dd-mm-aaaa: ")

      try:
         fecha = dt.datetime.strptime(fecha, "%d-%m-%Y")
         return fecha
      except ValueError as e:
        print(f"Ingrese una fecha válida. Error: {e}")

#--------------------------------------------------------------------------
#   Función que toma y valida el formato adecuado para un correo (Amaniel)
#--------------------------------------------------------------------------

def validar_email() -> None:

    while True:
        
        email = input("Correo electrónico: ")

        if email == "":
            return email
        elif not re.match(r"^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$", email):
            print("Debe ingresar un correo válido")
        else:
            return email

#----------------------------------------------------------------------------------------
#   Función que comprueba si el correo ingresado ya se encuentra en la lista (Amaniel)
#----------------------------------------------------------------------------------------

def check_email(email: str, lista: list) -> int:

    for c, p in enumerate(lista):
        if email == p.correo:
            return c
    return -1
    
#-------------------------------------------------------------------------------------
#   Función para validar una fecha en formato dd-mm-aaaa. Solo 1 intento (Amaniel)
#-------------------------------------------------------------------------------------

def fecha(s: str) -> str:
   
    fecha = input(f"Ingrese {s} en formato dd-mm-aaaa: ")

    try:
        fecha = dt.datetime.strptime(fecha, "%d-%m-%Y")
        return fecha
    except:
        pass