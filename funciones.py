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
        
#------------------------------------------------------
#   Función que carga la informacion desde CSV
#   y si no existe, crea uno nuevo (Brayan)
#------------------------------------------------------

def cargar_info(lista: list) -> None:

    try:
        with open('csv_lista.csv', 'rt') as doc:
            lines = csv.reader(doc, delimiter='|')
            next(lines, None)
            if lines == "":
                print("")
                print("Error. Archivo CSV vacio. No hay lista de participantes para cargar")
                return
            for l in lines:
                n_participante = Participante(l[0], l[1], l[2], l[3], l[4])
                lista.append(n_participante)
                print("")
            print("Lista de participantes cargada con exito")
        return
    
    except FileNotFoundError as e:
        print("")
        print(f"Error: {e}. Se creará un nuevo archivo CSV")
        with open('csv_lista.csv', 'wt', newline='') as doc:
            csvout = csv.writer(doc, delimiter='|')
            csvout.writerow(["Correo", "Nombre", "Fecha de nac."])
        return
    
#--------------------------------------------------------------------------
#   Función que registra a un nuevo participante (Brayan)
#--------------------------------------------------------------------------

def registrar_participante(lista: list) -> None:

    while True:
        print("")
        email = validar_email()
        if email == "":
            break
        if check_email(email, lista) != -1:
            print("")
            print("Ese correo ya está registrado")
            break
        elif check_email(email, lista) == -1:
            nombre = get_nombre()
            f_nac = get_fecha("su fecha de nacimiento")
            f_nac_form = f_nac.strftime("%d-%m-%Y")
            f_reg = dt.date.today()
            f_reg_form = f_reg.strftime("%d-%m-%Y")
            h_reg = dt.datetime.now()
            h_reg_form = h_reg.strftime("%H:%M:%S")
            lista.append(Participante(email, nombre, f_nac_form, f_reg_form, h_reg_form))
            print("")
            print("Participante registrado con éxito")
            return
    return

#--------------------------------------------------------------------------
#   Función que busca la información de un participante (Brayan)
#--------------------------------------------------------------------------

def buscar_participante(lista: list) -> None:

    if len(lista) == 0:
        print("")
        print("No hay participantes registrados")
        return
    
    while True:
        print("")
        email = validar_email()
        if email == "":
            break
        for c in lista:
            if email == c.correo:
                ancho = max(len(str(c.correo)), len(str(c.nombre)), len(str(c.fecha_nac)), len(str(c.fecha_reg)), len(str(c.hora_reg)))
                ancho += 3
                print(f"{"Nombre": <{ancho}} | {"Correo": <{ancho}} | {"F. de nac.": <{ancho}} | {"F. de registro": <{ancho}} | {"Hora de reg.": <{ancho}}")
                print(f"{c.nombre: <{ancho}} | {c.correo: <{ancho}} | {c.fecha_nac: <{ancho}} | {c.fecha_reg: <{ancho}} | {c.hora_reg: <{ancho}}")
                return 
            else:
                print("")
                print("No hay un participante con ese correo registrado")
                return

            
#--------------------------------------------------------------------------
#   Función para modificar la información de un participante (Brayan)
#--------------------------------------------------------------------------

def mod_participante(lista: list) -> None:

    while True:
        if len(lista) == 0:
            print("")
            print("No hay participantes registrados")

        print("")
        email = validar_email()

        if email == "":
            break

        for c in lista:
            if email == c.correo:

                print("")
                print("Si no relizará cambios en un atributo, solo presione Enter")
                n_correo = validar_email()
                n_nombre = get_nombre()
                n_fecha_nac = fecha("fecha de nacimiento")

                if n_correo:
                    c.correo = n_correo
                if n_nombre:
                    c.nombre = n_nombre
                if n_fecha_nac:
                    c.fecha_nac = n_fecha_nac.strftime("%d-%m-%Y")

                print("")
                print("Datos actualizados exitosamente")
                return
            
            print("No hay un participante registrado con ese correo")
