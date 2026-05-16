# -------------------------------------------------------------------------
# Modulo en el que definimos e incializamos la clase Participante (Jesus)
# -------------------------------------------------------------------------

from datetime import date, time

class Participante:
    correo = ""
    nombre = ""
    fecha_nac = ""
    fecha_reg = ""
    hora_reg = ""

    def __init__(self, correo: str, nombre: str, fecha_nac: date, fecha_reg: date, hora_reg = time):
        self.correo = correo
        self.nombre = nombre
        self.fecha_nac = fecha_nac
        self.fecha_reg = fecha_reg
        self.hora_reg = hora_reg
        
    def __str__(self):
        salida = f"""Correo: {self.correo}
Nombre: {self.nombre}
Fecha de nac.: {self.fecha_nac}
Fecha de reg.: {self.fecha_reg}
Hora de reg.: {self.hora_reg}"""
        return salida
