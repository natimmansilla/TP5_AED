import pickle

from Evento import Evento
from Evento import generar_aleatorio
import os

def menu():
    print()
    opciones = ("====MENU DE OPCIONES====\n"
                "1. Generar un arreglo de objetos.\n"
                "2. Mostrar el arreglo.\n"
                "3. Generar un archivo binario.\n"
                "4. Mostrar los datos de un archivo binario.\n"
                "5. Generar un vector de acumulación.\n"
                "6. Busqueda binaria por codigo.\n"
                "7. Generar matriz de conteo por tipo de evento y segmento diario.\n"
                "8. Analisis de caracteres.\n"
                "0. Salir.\n"
                "====> Ingrese su opción: ")
    return int(input(opciones))


def validar_mayor_que(limite, mensaje="Ingrese un numero: "):
    numero = limite
    while numero <= limite:
        numero = int(input(mensaje))
        if numero <= limite:
            print("ERROR! Debe ingresar un numero mayor que {}".format(limite))
    return numero


#PUNTO 1
def generar_vector(vec, n):
    for i in range(n):
        evento = generar_aleatorio()
        add_in_order(evento, vec)
    print("Los eventos fueron cargados exitosamente...")

def add_in_order(evento, vec):
    n = len(vec)
    izq, der = 0, n - 1
    pos = -1
    while izq <= der:
        c = (izq + der) // 2
        if evento.codigo == vec[c].codigo:
            pos = c
        if evento.codigo < vec[c].codigo:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    vec[pos:pos] = [evento]

# PUNTO 2
def mostrar_vector(vec):
    for eventos in vec:
        print(eventos)

# PUNTO 3
def generar_archivo_binario(vec, archivo_binario):
    mb = open(archivo_binario, "wb")
    for eventos in vec:
        pickle.dump(eventos, mb)

    mb.close()
    print("Archivo binario exitosamente generado...")

def mostrar_archivo_binario(archivo_binario):
    if os.path.exists(archivo_binario):
        mb = open(archivo_binario, "rb")
        tam = os.path.getsize(archivo_binario)
        while mb.tell() < tam:
            evento = pickle.load(mb)
            print(evento)

        mb.close()
    else:
        print("El archivo binario {} no existe...".format(archivo_binario))


# PUNTO 4
def generar_vector_acumulacion(vec_acum, archivo_binario):
    if os.path.exists(archivo_binario):
        mb = open(archivo_binario, "rb")
        tam = os.path.getsize(archivo_binario)

        while mb.tell() < tam:
            evento = pickle.load(mb)

            if evento.tipo_evento >= 5:
                vec_acum.append(evento.costo)

        mb.close()
    else:
        print("El archivo binario {} no existe...".format(archivo_binario))


def mostrar_vector_acumulacion(vec_acum):
    contador_eventos = 0
    acumulador_costo = 0
    promedio = 0
    for eventos in vec_acum:
        contador_eventos += 1
        acumulador_costo += eventos
        print("Costo: $ ", eventos)

    if contador_eventos != 0:
        promedio = round(acumulador_costo / contador_eventos, 2)

    print("El promedio de los montos mostrados es de $ {}".format(promedio))


# PUNTO 5
def validar_codigo(mensaje="Ingrese un mensaje: "):
    codigo = ""
    while len(codigo) != 9:
        codigo = input(mensaje)
        if len(codigo) != 9:
            print("ERROR! Los códigos de los eventos tienen 9 caracteres alfanuméricos! ")
    return codigo


def busqueda_binaria_x_codigo(cod, vec):
    n = len(vec)
    pos = -1
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2

        if cod == vec[c].codigo:
            pos = c
            break
        if cod < vec[c].codigo:
            der = c - 1
        else:
            izq = c + 1
    return pos


# PUNTO 7
def cargar_matriz_conteo(mat_conteo, vec):
    """
    fila = tipo_evento = [0;19] => 20
    columna = segmento = [0;9] => 10
    total 10*20 = 200 contadores
    """
    mat = [[0]*10 for i in range (20)]
    for evento in vec:
        fila = evento.tipo_evento
        columna = evento.segmento
        mat[fila][columna] += 1


def varlidar_rango(inferior, superior, mensaje="Ingrese un numero: "):
    numero = inferior
    while numero < inferior or numero > superior:
        numero = int(input(mensaje))
        if numero < inferior or numero > superior:
            print("ERROR! Debe ingresar un numero que sea mayor o igual que {} y menor o igual que {}."
                  .format(inferior, superior))
    return numero

def mostrar_matriz_conteo(mat_conteo, te):
    for i in range(len(mat_conteo)):
        for j in range(len(mat_conteo[i])):
            if evento.tipo_evento > te:
                print("Para el tipo de evento {} y el segmento diario {}, los eventos son: {}"
                      .format(i, j, mat_conteo[i][j]))


# PUNTO 8
def calcular_cantidad_palabras(cadena):
    # inicializador de contadores, acumuladores y banderas no reiniciables
    cp = cp1 = 0

    # inicializador de contadores, acumuladores y banderas reiniciables
    ccp = 0
    b_start_mayus = False
    c_tiene_t = c_tiene_s = 0

    for car in cadena:
        if car != " " and car != ".":  # analizo caracteres
            ccp += 1

            if ccp == 1:
                if es_mayuscula(car):
                    b_start_mayus = True

            if car.lower() == "t":
                c_tiene_t += 1

            if car.lower() == "s":
                c_tiene_s += 1

        else: # analizo palabras
            if ccp > 0:
                cp += 1
                if b_start_mayus and (c_tiene_t > 0) and (c_tiene_s > 0):
                    cp1 += 1

            # reinicio de contadores, acumuladores y banderas
            ccp = 0
            b_start_mayus = False
            c_tiene_t = c_tiene_s = 0

    return cp1


def es_mayuscula(c):
    return "A" <= c <= "Z" or c == "Ñ"


def principal():
    vec = []
    mat_conteo = []
    op = -1
    archivo_binario = "eventos.dat"

    while op != 0:
        op = menu()

        if op == 1:
            n = validar_mayor_que(0, "Ingrese la cantidad de eventos: ")
            generar_vector(vec, n)

        elif vec != []:

            if op == 2:
                mostrar_vector(vec)

            elif op == 3:
                generar_archivo_binario(vec, archivo_binario)

            elif op == 4:
                mostrar_archivo_binario(archivo_binario)

            elif op == 5:
                vec_acum = []
                generar_vector_acumulacion(vec_acum, archivo_binario)
                mostrar_vector_acumulacion(vec_acum)

            elif op == 6:
                cod = validar_codigo("Ingrese el código a buscar: ")
                pos = busqueda_binaria_x_codigo(cod, vec)
                if pos != -1:
                    print(vec[pos])
                    print("Descripcion del evento: ", vec[pos].descripcion)
                else:
                    print("El codigo {} no se encontró.".format(cod))

            elif op == 7:
                cargar_matriz_conteo(mat_conteo, vec)
                # te es un tipo de evento [0;19] que se carga por teclado
                te = varlidar_rango(0, 19, "Ingrese el tipo de evento a discriminar: ")
                mostrar_matriz_conteo(mat_conteo, te)

            elif op == 8:
                cadena = vec[pos].descripcion
                contador_palabras = calcular_cantidad_palabras(cadena)

                print("La cantidad de palabras que empiezan con mayúscula, contienen una letra t y una letra s son {}"
                      .format(contador_palabras))
        elif op == 0:
            print("Fin del programa! ")
        else:
            print("Debe cargar los eventos primero! Ingrese la opción 1.")


if __name__ == '__main__':
    principal()
