import random


class Evento:
    def __init__(self, codigo, titulo, descripcion, costo, tipo_evento, segmento):
        self.codigo = codigo
        self.titulo = titulo
        self.descripcion = descripcion
        self.costo = costo
        self.tipo_evento = tipo_evento
        self.segmento = segmento

    def __str__(self):
        return "ID: {:5} | Titulo: {:5} | Descripción: {:5} | Costo: {:5} | Tipo de Evento: {:5} |" \
               " Segmento diario: {:5} "\
            .format(self.codigo, self.titulo, self.descripcion, self.costo, self.tipo_evento, self.segmento)

def generar_aleatorio():
    letras = ("A","B","C","D","E"FGHIJKLMNÑOPQRSTUVWXYZ")
    codigo = random.choice(letras)