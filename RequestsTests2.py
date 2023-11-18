

my_cursor = mydb.cursor()

empresas = []

def mostrar_empresas(tabla):
    my_cursor.execute("SELECT nombre FROM " + tabla)
    my_result = my_cursor.fetchall()
    print("¿De qué empresa prefieres sacar la información?")

    for i in my_result:
        print("-", i)
        empresas.append(i)

def validar_existencia_empresa():
    empresa_existe = None
    while empresa_existe == None or empresa_existe == False:
        if empresa_existe == False:
            print("La empresa elegida no existe, por favor elige una válida.")

        empresa_elegida = input()
        for i in empresas:
            if empresa_elegida == i:
                empresa_existe = True
                break
            else:
                empresa_existe = False
    
    return empresa_existe

def mostrar_opciones():
    for i in op:
        print(i)

def ver_datos_tabla(tabla):
    my_cursor.execute("SELECT * FROM " + tabla)
    my_result = my_cursor.fetchall()
    for i in my_result:
        print(i)


def ver_datos_campo(tabla):
    print("¿De qué campo?\nCampos disponibles:")
    my_cursor.execute("SHOW COLUMNS FROM " + tabla)
    my_result = my_cursor.fetchall()

    columnas = []
    # Mostramos el nombre de las columnas
    for i in range(len(my_result)):
        # El elemento de la posición 0 es le nombre de la columna, el resto son otros datos
        print("-", my_result[i][0])
        columnas.append(my_result[i][0])

    # Comprobamos que la columna elegida existe y si no, seguiremos pidiendo hasta que el usuario proporcione una correcta
    columna_existe = False
    while columna_existe == False:
        columna_elegida = input("Columna elegida -> ")

        for i in columnas:
            if columna_elegida == i:
                my_cursor.execute("SELECT " + columna_elegida + " FROM " + tabla)
                my_result = my_cursor.fetchall()
                for i in my_result:
                    print(i)

                columna_existe = True
            else:
                print("El campo elegido no existe. Por favor elige uno que sí lo haga.")

def realizar_acciones_basicas(tabla):
    mostrar_opciones()
    op = input()
    if op == "a":
        ver_datos_tabla(tabla)
    elif op == "b":
        ver_datos_campo(tabla)
    else:
        print("Opción no válida. Elige una correcta.")
        consultar_registro(tabla)


def consultar_registro(tabla):
    if tabla == "Puntos de venta":
        op.extend(["c) Ver las ventas que tiene una tienda por su id (1-8 incluidos) y las características de los videjuegos que ha vendido"])
        mostrar_opciones()

        op_puntos_venta = input()
        if op_puntos_venta == "a":
            ver_datos_tabla(tabla)

        elif op_puntos_venta == "b":
            ver_datos_campo(tabla)

        elif op_puntos_venta == "c":
            id_correcto = None

            while id_correcto == None:
                id = int(
                    input("Introduce un ID (un número del 1 al 8 incluidos): "))
                try:
                    if id < 1 or id > 8:
                        print("Número fuera de rango.")
                    else:
                        # TODO CONFIRMAR LA RELACION CON ARRAYS (String largo)
                        # El id introducido es uno correcto, por tanto...
                        my_cursor.execute("SELECT puntos_de_venta.ventas, videojuegos.* FROM " + tabla + "JOIN videojuegos on puntos_de_venta.videojuegos = videojuegos.id" + " WHERE id = " + id)
                        id_correcto = True
                except TypeError:
                    print(
                        "No se permiten datos que no sean números enteros, por favor introduce uno válido.")

        else:
            print("Opción no válida. Elige una correcta.")
            consultar_registro(tabla)

    elif tabla == "videojuegos":
        realizar_acciones_basicas(tabla)
    
    elif tabla == "generos":
        realizar_acciones_basicas(tabla)

    elif tabla == "empresa":

        op.extend(["c) Ver las características de un empleado de un equipo de una empresa"], ["d) Ver características de los videojuegos que ha producido una empresa"])
        mostrar_opciones()

        op_empresa = input()
        if op_empresa == "a":
            ver_datos_tabla(tabla)
        elif op_empresa == "b":
            ver_datos_campo(tabla)
        elif op_empresa == "c":
            empresa_elegida = None
            equipo_elegido = None
            clase_empleado = None
            empleado_elegido = None

            # PROCESO DE ELECCIÓN DE EMPRESA
            mostrar_empresas(tabla)
            empresa_existe = None
            while empresa_existe == None or empresa_existe == False:
                if empresa_existe == False:
                    print("La empresa elegida no existe, por favor elige una válida.")

                empresa_elegida = input()
                for i in empresas:
                    if empresa_elegida == i:
                        empresa_existe = True
                        break
                    else:
                        empresa_existe = False
            
            # Como empresa_existe es True, no hace falta que hagamos un  condicional para ejecutar lo siguiente
            # PROCESO DE ELECCIÓN DE EQUIPO
            print("Elige un equipo del 1 al 16")
            equipos = []
            for i in range(1, 16):
                equipos.append(i)

            equipo_existe = None
            while equipo_existe == None or equipo_existe == False:
                if equipo_existe == False:
                    print("El equipo elegido no existe, por favor elige uno válido.")

                equipo_elegido = int(input())
                for i in equipos:
                    if equipo_elegido == i:
                        equipo_existe = True
                        break
                    else:
                        equipo_existe = False

            # PROCESO DE ELECCIÓN DE EMPLEADO
            print("¿Qué quieres que sea tu empleado?")
            empleados = ["a) Animador", "b) Artista", "c) Programador", "d) Compositor"]
            for i in empleados:
                print(i)
            clase = None

            clase_empleado_existe = None
            while clase_empleado_existe == None or clase_empleado_existe == False:
                clase_empleado = input()

                if clase_empleado.lower() == "a":
                    clase_empleado_existe == True
                    clase = "animadores"
                elif clase_empleado.lower() == "b":
                    clase_empleado_existe == True
                    clase = "artistas"
                elif clase_empleado.lower() == "c":
                    clase_empleado_existe == True
                    clase = "programadores"
                elif clase_empleado.lower() == "d":
                    clase_empleado_existe == True
                    clase = "compositores"
                else:
                    clase_empleado_existe = False
                    print("La clase de empleado elegida no existe, por favor elige una válida.")
            
            while True:
                empleado_elegido = int(input("Elige uno del 1 al 32 -> "))
                if empleado_elegido < 1  or empleado_elegido > 32:
                    print("Número de empleado fuera de rango.")
                else:
                    break

            # TODO CONSULTA FINAL
            my_cursor.execute("SELECT " + clase + ".* FROM " + tabla + " JOIN equipos ON " + tabla +
            ".equipos = equipos.id JOIN " + clase + " ON equipos." + clase + " = " + clase 
            + "id WHERE " + tabla + ".nombre = " + empresa_elegida + " && equipos.id = " + equipo_elegido +
            " && " + clase + ".id = " + empleado_elegido)

            my_result = my_cursor.fetchall()
            # Impreso por pantalla
            for i in my_result:
                print(i)

        elif op_empresa == "d":
            # MAL, TODO Averiguar cómo coger los elementos del Array (Strings) y relacionarlos con la tabla 'videojuegos' para coger las características de estos pertenecientes a una empresa
            # PROCESO DE ELECCIÓN DE EMPRESA
            mostrar_empresas(tabla)
            empresa_elegida = None
            empresa_existe = None
            while empresa_existe == None or empresa_existe == False:
                if empresa_existe == False:
                    print("La empresa elegida no existe, por favor elige una válida.")

                empresa_elegida = input()
                for i in empresas:
                    if empresa_elegida == i:
                        empresa_existe = True
                        break
                    else:
                        empresa_existe = False
            
            my_cursor.execute("SELECT videojuegos.* FROM " + tabla + " JOIN videojuegos ON videojuegos.id = " +
            tabla + ".videojuegos WHERE " + tabla + ".nombre = " + empresa_elegida)

            my_result = my_cursor.fetchall()
            # Impreso por pantalla
            for i in my_result:
                print(i)

        else:
            print("Opción no válida. Elige una correcta.")
            consultar_registro(tabla)

    elif tabla == "equipos":
        realizar_acciones_basicas(tabla)
    
    elif tabla == "artistas":
        realizar_acciones_basicas(tabla)

    elif tabla == "animadores":
        realizar_acciones_basicas(tabla)
    
    elif tabla == "programadores":
        realizar_acciones_basicas(tabla)

    elif tabla == "compositores":
        realizar_acciones_basicas(tabla)

def anadir_registro(tabla):
    my_cursor.execute("SHOW COLUMNS FROM " + tabla)
    my_result = my_cursor.fetchall()

    request = "INSERT INTO " + tabla + "VALUES ("

    # Vamos construyendo la instrucción, mostrándo al usuario lo que tiene que intoducir y controlando que introduzca
    # tipos de datos correctos
    for i in range(len(my_result)):
        while True:
            request_piece = input(my_result[i][0], "-> ") # Vamos mostrando los nombres de las columnas
            if my_result[i][1] == "int":
                if request_piece.isnumeric() == False:
                    print("Se necesita un número entero.")
            elif my_result[i][1] == "varchar" or my_result[i][1] == "char":
                if request_piece.isnumeric() == True:
                    print("Se necesita una cadena de texto.")
            
            campos_comprobar_longitud = ("videojuegos", "generos", "equipos", "artistas", "animadores", "programadores", "compositores")
            longitud_correcta = False

            for i in campos_comprobar_longitud:
                if my_result[i][0] == i:
                    my_cursor.execute("SELECT COUNT(*) FROM " + i)
                    mi_resultado = my_cursor.fetchall()

                    if int(request_piece) > mi_resultado[0][0]:
                        print("El " + i + "elegido no existe, debes insertarlo en la tabla '" + i + "' previamente si deseas añadirlo en este campo.")
                    else:
                        longitud_correcta = True
                break

            if longitud_correcta == True:
                break
            
        request += request_piece + ", "

    # Cuando se finaliza de construir la instrucción, tenemos que quitar la "coma y espacio" del final para que sea una
    # instrucción válida, por lo que metemos request en una lista para quitar los dos ultimos elementos y luego enviamos
    # los elementos de esa lista uno por uno a request para formar la request final
    request_list = []
    for i in range(len(request)):
        request_list.append(i)

    request_list.pop()
    request_list.pop()

    request = ""
    for i in request_list:
        request += i

    my_cursor.execute(request)
    # mydb.commit()

# ELIMINAR REGISTRO HECHO
def eliminar_registro(tabla):
    print("Deseas eliminar todos los registros de la tabla (presiona A) o uno en concreto (presiona B)")
    op_registros = input()

    if op_registros.lower() == "a":
        my_cursor.execute("DELETE FROM " + tabla)
        # mydb.commit()
    elif op_registros.lower() == "b":
        my_cursor.execute("SELECT COUNT(*) FROM " + tabla)
        my_result = my_cursor.fetchall()

        while True:
            print("Elige un identificador del 1 al " + my_result[0])
            identificador = int(input())

            try:
                if identificador < 1 or identificador > my_result[0]:
                    print("Identificador fuera de rango.")
                else:
                    break
            except TypeError:
                print("Se necesita un valor numérico")

        my_cursor.execute("DELETE FROM " + tabla + " WHERE id = " + identificador)
        # mydb.commit()
    else:
        print("Opción nó válida.")
        eliminar_registro(tabla)

# MODIFICAR REGISTRO HECHO
def modificar_registro(tabla):
    print("¿Qué campo quieres modificar?")
    my_cursor.execute("SHOW COLUMNS FROM " + tabla)
    my_result = my_cursor.fetchall()

    claves_columnas = {}
    tipo_dato_columnas = {}
    # Hacer un diccionario que relacione la cifra "i" (clave) con "my_result" (valor) para luego acceder
    # rápidamente a los campo mediante su "clave"
    for i in range(1, len(my_result)):
        print(i, "-", my_result[i][0])
        claves_columnas[i] = my_result[i][0]
        tipo_dato_columnas[i] = my_result[i][1]
    
    campo_a_modificar = None
    nuevo_valor = None
    while True:
        campo_a_modificar = int(input("Elige tu campo -> "))
        try:
            if campo_a_modificar < 1 or campo_a_modificar > len(claves_columnas):
                print("Campo no existente.")
            else:
                break

        except TypeError:
            print("Se necesita un campo numérico.")

    while True:
        nuevo_valor = input("Nuevo valor para", claves_columnas[campo_a_modificar], "-> ")
        if tipo_dato_columnas[campo_a_modificar] == "int":
            if nuevo_valor.isnumeric() == False:
                print("Se necesita un valor numérico.")
            else:
                break
        else:
            if nuevo_valor.isnumeric() == True:
                print("Se necesita un valor de texto.")
            else:
                break
    my_cursor.execute("UPDATE " + tabla + " SET", claves_columnas[campo_a_modificar], "=", nuevo_valor)
    # mydb.commit()

# CREAR TABLA HECHO
def crear_tabla():
    nombre_tabla = input("Nombre de tu nueva tabla -> ")
    num_columnas = None

    while True:
        try:
            num_columnas = int(input("Numero de columnas de tu tabla -> "))
            if num_columnas > 0:
                break
            else:
                print("Se necesita un valor positivo.")
        except TypeError:
            print("Se necesita un valor numérico.")
    
    nombre_y_tipo = ""
    coma_espacio = ", "

    for i in range(num_columnas):
        nombre_campo = (input("Nombre del campo", i + 1, "-> ")).upper()
        tipo_dato_campo = (input("Tipo de dato del campo", i + 1, "-> ")).upper()

        if tipo_dato_campo == "VARCHAR" or tipo_dato_campo == "CHAR" or tipo_dato_campo == "INT":
            while True:
                longitud = input("Longitud -> ")
                if longitud.isnumeric():
                    break
                else:
                    print("Se necesita un valor numérico.")
            nombre_y_tipo += nombre_campo + " " + tipo_dato_campo + " (" + longitud + ")"
        else:
            nombre_y_tipo += nombre_campo + " " + tipo_dato_campo

        if i != (num_columnas - 1):
            nombre_y_tipo += coma_espacio

    my_cursor.execute("CREATE TABLE IF NOT EXISTS" + nombre_tabla + " (" + nombre_y_tipo + ")")

# BORRAR TABLA HECHO
def borrar_tabla(tabla):
    my_cursor.execute("DROP TABLE IF EXISTS " + tabla)



# EL PROGRAMA PRINCIPAL EMPIEZA AQUÍ

# Listamos las opciones con las que trabajar
tablas = ["Puntos de venta", "Videojuegos", "Generos", "Empresa",
          "Equipos", "Artistas", "Animadores", "Programadores", "Compositores"]

print("Hola.")

decision_existe = False

while decision_existe == False:
    print("¿Quieres crear una tabla (a) o trabajar con una ya existente (b)?")
    crear_trabajar_decision = input()

    if crear_trabajar_decision.lower() = "a":
        crear_tabla()
        decision_existe = True
    elif crear_trabajar_decision.lower() = "b":
        print("Tablas disponibles con las que trabajar: ")
        for i in tablas:
            print("-", i)

        # Si la tabla elegida no exixte, seguiremos pidiendo hasta obtener una correcta
        # Cuando haya una coincidencia, convierte en minúsculas las cosas a comparar para asegurarnos de que las mayusculas no produzcan errores
        tabla_existe = None
        while tabla_existe == None or tabla_existe == False:
            if tabla_existe == False:
                print("La tabla elegida no existe.")
            tabla_elegida = input("Elige una -> ")

            for i in tablas:
                if tabla_elegida.lower() == i.lower():
                    tabla_existe = True
                    break
                else:
                    tabla_existe = False

        # Formateamos la opción elegida para que la primera letra sea mayúscula y el resto sea minúscula
        tabla_elegida_letras = []
        for i in range(len(tabla_elegida)):
            if i == 0:
                tabla_elegida_letras.append(tabla_elegida[i].upper())
            else:
                tabla_elegida_letras.append(tabla_elegida[i].lower())

        tabla_elegida = ""
        for i in tabla_elegida_letras:
            tabla_elegida += i

        # Una vez formateada la opción, damos la oportunidades de trabajar con la tabla seleccionada
        # Si el usuario elige una opción no válida, seguiremos pidiendo hasta que de una correcta
        opcion_valida = None
        while opcion_valida == None:
            print("¿Qué deseas hacer con '" + tabla_elegida +
                "', consultar (a), añadir (b), eliminar (c) o modificar (d) un registro, o bien, borrarla (e)?")
            eleccion = input()

            global op
            op = ["a) Ver toda la informacion", "b) Ver la información de un campo"]
            print("\nOpciones:")

            if eleccion == "a":
                consultar_registro(tabla_elegida)
                opcion_valida = True
            elif eleccion == "b":
                anadir_registro(tabla_elegida)
                opcion_valida = True
            elif eleccion == "c":
                eliminar_registro(tabla_elegida)
                opcion_valida = True
            elif eleccion == "d":
                modificar_registro(tabla_elegida)
                opcion_valida = True
            elif eleccion == "e":
                borrar_tabla(tabla_elegida)
                opcion_valida = True
            else:
                print("La opción elegida no es válida. Elige una que sí lo sea.")
        decision_existe = True

    else:
        print("La decisión elegida no existe.")

print("Fin de la conexión.")