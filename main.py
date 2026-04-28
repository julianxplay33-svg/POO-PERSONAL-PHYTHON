from enum import Enum

class EstadoTarea(Enum):
    PENDIENTE = "pendiente"
    EN_PROGRESO = "en progreso"
    TERMINADA = "terminada"
    EN_REVISION = "en revision"
class Tarea:
    def __init__(self, nombre, responsable):
        self.nombre = nombre
        self.responsable = responsable
        self.estado = EstadoTarea.PENDIENTE

    def set_estado(self, estado):
        self.estado = estado

    def get_estado(self):
        return self.estado
