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
        return "ID: {:<10} | Titulo: {:<15} | Descripción: {:<88} | Costo: $ {:<13} | Tipo de Evento: {:<4} |" \
               " Segmento diario: {:<3} "\
            .format(self.codigo, self.titulo, self.descripcion, self.costo, self.tipo_evento, self.segmento)


def generar_codigo():
    letras = ("AED", "JCB", "ETC", "HID", "OPE", "YQF", "AGX", "BGH", "OPÑ")
    codigo = random.choice(letras) + random.choice(letras) + str(random.randint(100, 999))
    return codigo


def generar_titulo():
    secciones = ("Informativo", "Último minuto", "Recordatorio", "Aviso Urgente")
    titulos = random.choice(secciones)
    return titulos


def generar_descripcion(titulo):
    descripcion = ""
    token = random.randint(1, 2)
    if titulo == "Informativo":
        if token == 1:
            descripcion = "Precio de BTC cae por sobrecalentamiento de derivados de bitcoin."
        elif token == 2:
            descripcion = "Encontró un barco de 1886 sepultado en Tigre y hoy viaja para devolverlo a su tierra."

    elif titulo == "Último minuto":
        if token == 1:
            descripcion = "Fifa confirmó las 16 sedes que tendrá el Mundial 2026."
        if token == 2:
            descripcion = "El terremoto tuvo su epicentro en San Juan y se sintió en todo el norte argentino."

    elif titulo == "Recordatorio":
        if token == 1:
            descripcion = "Ya estan abiertas las convocatorias para el financiamiento de proyectos tecnológicos."
        elif token == 2:
            descripcion = "Hasta el viernes 1 de diciembre podes inscribirte para el ingreso 2024 en la UTN."

    elif titulo == "Aviso Urgente":
        if token == 1:
            descripcion = "Cortes de ruta generan demoras en la Autopista Buenos Aires Rosario."
        elif token == 2:
            descripcion = "En Tartagal por faltante de combustible suspendieron el servicio de transporte."

    return descripcion


def generar_aleatorio():
    codigo = generar_codigo()
    titulo = generar_titulo()
    descripcion = generar_descripcion(titulo)
    costo = round(random.uniform(100000, 9999999), 2)
    tipo_evento = random.randint(0, 19)
    segmento = random.randint(0, 9)

    evento = Evento(codigo, titulo, descripcion, costo, tipo_evento, segmento)

    return evento
