from Evento import generar_aleatorio
import os
import pickle


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
            print("ERROR! Debe ingresar un número mayor a {}".format(limite))
    return numero


# PUNTO 1
def generar_vector(vec, n):
    for i in range(n):
        evento = generar_aleatorio()
        add_in_order(evento, vec)
    print("Los eventos fueron cargados exitosamente...")


# Inserta ordenadamente por código.
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
def generar_archivo_binario(vec, archivo_binario, p):
    # p es un monto/costo de producción cargado por teclado
    mb = open(archivo_binario, "wb")
    for eventos in vec:
        if eventos.costo > p:
            pickle.dump(eventos, mb)

    mb.close()
    print("Archivo binario exitosamente generado...")


def varlidar_rango_float(inferior, superior, mensaje="Ingrese un número: "):
    numero = inferior - 1
    while numero < inferior or numero > superior:
        numero = float(input(mensaje))
        if numero < inferior or numero > superior:
            print("ERROR! Debe ingresar un número que sea mayor o igual que {} y menor o igual que {}."
                  .format(inferior, superior))
    return numero


# PUNTO 4
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


# PUNTO 5
def generar_vector_costo(vec_costo, archivo_binario):
    if os.path.exists(archivo_binario):
        mb = open(archivo_binario, "rb")
        tam = os.path.getsize(archivo_binario)

        while mb.tell() < tam:
            evento = pickle.load(mb)

            if evento.tipo_evento >= 5:
                vec_costo.append(evento.costo)

        mb.close()
    else:
        print("El archivo binario {} no existe...".format(archivo_binario))


def mostrar_vector_costo(vec_costo):
    contador_eventos = 0
    acumulador_costo = 0
    promedio = 0
    for eventos in vec_costo:
        contador_eventos += 1
        acumulador_costo += eventos
        print("Costo: $ ", eventos)

    if contador_eventos != 0:
        promedio = round(acumulador_costo / contador_eventos, 2)
    print()
    print("El promedio de los montos mostrados es de $ {}".format(promedio))


# PUNTO 6
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

    if pos != -1:
        print(vec[pos])
        des = vec[pos].descripcion
        return des
    else:
        print("El código {} no se encontró.".format(cod))
        return "No existe."


# PUNTO 7
def cargar_matriz_conteo(vec):
    """
    fila = tipo_evento = [0;19] => 20
    columna = segmento = [0;9] => 10
    total 10*20 = 200 contadores
    """
    mat_conteo = [[0]*10 for i in range(20)]
    for evento in vec:
        fila = evento.tipo_evento
        columna = evento.segmento
        mat_conteo[fila][columna] += 1

    return mat_conteo


def varlidar_rango_int(inferior, superior, mensaje="Ingrese un número: "):
    numero = inferior - 1
    while numero < inferior or numero > superior:
        numero = int(input(mensaje))
        if numero < inferior or numero > superior:
            print("ERROR! Debe ingresar un número que sea mayor o igual que {} y menor o igual que {}."
                  .format(inferior, superior))
    return numero


def mostrar_matriz_conteo(mat_conteo, te):
    for i in range(len(mat_conteo)):
        for j in range(len(mat_conteo[i])):
            if i > te and mat_conteo[i][j] > 0:
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

        # Analizo palabras
        else:
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
    print()
    vec = []
    op = -1
    archivo_binario = "eventos.dat"
    b_pto_6 = False
    desc = ""

    while op != 0:
        op = menu()

        if op == 1:
            n = validar_mayor_que(0, "Ingrese la cantidad de eventos: ")
            generar_vector(vec, n)

        elif vec != []:

            if op == 2:
                mostrar_vector(vec)

            elif op == 3:
                # p es un monto/costo de producción cargado por teclado
                p = varlidar_rango_float(100000, 9999999, "Ingrese el monto mínimo de "
                                                          "producción: ")
                generar_archivo_binario(vec, archivo_binario, p)

            elif op == 4:
                mostrar_archivo_binario(archivo_binario)

            elif op == 5:
                vec_costo = []
                generar_vector_costo(vec_costo, archivo_binario)
                mostrar_vector_costo(vec_costo)

            elif op == 6:
                b_pto_6 = True
                cod = validar_codigo("Ingrese el código a buscar: ")
                # desc contiene la cadena str del atributo descripcion o en su defecto la cadena "No existe."
                desc = busqueda_binaria_x_codigo(cod, vec)

            elif op == 7:
                mat_conteo = cargar_matriz_conteo(vec)

                # te es un tipo de evento [0;19] que se carga por teclado
                te = varlidar_rango_int(0, 19, "Ingrese el tipo de evento mínimo: ")
                mostrar_matriz_conteo(mat_conteo, te)

            elif b_pto_6:
                if op == 8:
                    if desc != "No existe.":
                        contador_palabras = calcular_cantidad_palabras(desc)
                        print("La cantidad de palabras que empiezan con mayúscula, contienen una letra t y una letra s "
                              "son {}".format(contador_palabras))
                    else:
                        print("La descripción del evento asociada al código buscado en el punto 6 {}"
                              " ya que el código no fue encontrado.".format(desc))
            else:
                print("Debe cargar la descripción antes. Ingrese la opción 6.")

        elif op == 0:
            print("Fin del programa! ")

        else:
            print("Debe cargar los eventos primero! Ingrese la opción 1.")


if __name__ == '__main__':
    principal()
