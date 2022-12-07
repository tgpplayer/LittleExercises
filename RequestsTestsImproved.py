import Usuario

my_cursor = mydb.cursor()

empresas = []

def mostrar_empresas(tabla):
    my_cursor.execute("SELECT nombre FROM " + tabla)
    my_result = my_cursor.fetchall()
    print("¿De qué empresa prefieres sacar la información?")

    for i in my_result:
        print("-", i)
        empresas.append(i)

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
    realizar_acciones_basicas(tabla)

# AÑADIR REGISTRO HECHO
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

            for j in campos_comprobar_longitud:
                if my_result[i][0] == j:
                    my_cursor.execute("SELECT COUNT(*) FROM " + j)
                    mi_resultado = my_cursor.fetchall()

                    if int(request_piece) > mi_resultado[0][0]:
                        print("El " + j + "elegido no existe, debes insertarlo en la tabla '" + j + "' previamente si deseas añadirlo en este campo.")
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
    request += ")"

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
                if claves_columnas[campo_a_modificar] == "videojuegos" or claves_columnas[campo_a_modificar] == "equipos" or claves_columnas[campo_a_modificar] == "artistas" or claves_columnas[campo_a_modificar] == "animadores" or claves_columnas[campo_a_modificar] == "programadores" or claves_columnas[campo_a_modificar] == "compositores":
                    my_cursor.execute("SELECT " + claves_columnas[campo_a_modificar] + " FROM " + tabla + 
                    "WHERE id = " + campo_a_modificar)
                    my_result = my_cursor.fetchall()

                    # Como este campo es un "array"(String separado los elementos por comas), necesitamos concatanar
                    # el valor que se quiere actualmente al valor que ya estaba registrado, por lo que:
                    nuevo_valor = my_result[0][0] + nuevo_valor
                    break
                else:
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


# FUNCIONES PARA LA PARTE DE USUARIOS
usuarios = []
roles_predeterminados = ["lector", "editor", "creador", "admin"]
roles = roles_predeterminados.copy()

consulta = edicion = creacion = borrado = None

def mostrar_usuarios():
    for i in range(len(usuarios)):
        print(i + 1, ")", usuarios[i].rol, "(" + usuarios[i].nick + ")")
        usuarios[i].mostrar_permisos()
        print("")

def mostrar_roles():
    for i in roles_predeterminados:
        print("-", i)

def usuario_existe():
    usuario = None
    while True:
        try:
            usuario = int(input())
            if usuario < 1 or usuario > len(usuarios):
                print("El usuario elegido no existe, por favor inserta uno que sí lo haga.")
            else:
                return usuario
        except:
            print("Se necesita un valor numérico entre 1 y", len(usuarios))

def crear_usuario():
    print("Elige un nick para este usuario.")

    nick = input("Nick -> ")

    rol_existe = False
    rol = None
    print("Roles disponibles:")
    mostrar_roles()

    while rol_existe == False:
        rol = input("Rol de tu nuevo usuario -> ")

        for i in roles_predeterminados:
            if rol.lower() == i:
                rol_existe = True
        if rol_existe == False:
            print("El rol elegido no existe.")

    usuario = Usuario.Usuario(rol, nick)
    usuario.set_permisos_iniciales()
    usuarios.append(usuario)

def borrar_usuario():
    # Mostramos usuarios para que luego el usuario decida cual borrar
    print("¿Qué usuario quieres borrar?")
    mostrar_usuarios()

    # 'usuario_existe' devuelve el numero que identifica al usuario, y mientras no exista, no dejará borrar tal usuario
    usuario = usuarios[usuario_existe() - 1]
    usuarios.remove(usuario) 
    print("Usuarios actuales:")
    mostrar_usuarios()

def modificar_usuario():
    print("¿Que usuario quieres modificar?")
    mostrar_usuarios()
    usuario = usuarios[usuario_existe() - 1]
    usuario.set_permisos_nuevos() # Esta es la función clave que modifica al usuario
    usuario.mostrar_permisos()

def crear_rol():
    if len(roles) < len(roles_predeterminados):
        print("¿Qué rol quieres crear?")
        mostrar_roles()
        rol_a_crear = None
        while True:
            rol_a_crear = input("Rol a crear -> ")
            # Se quiere que el rol a crear exista, y si existe que lo añada a roles, pero si roles ya tiene ese rol, no se premite
            if rol_a_crear not in roles_predeterminados:
                print("El rol elegido no es válido. Elige uno que si lo sea.")
            else:
                if rol_a_crear in roles:
                    print("El rol elegido ya existe. Elige uno que no lo haga")
                else:
                    roles.append(rol_a_crear)
                    print("Rol creado.\nRoles actuales:")
                    mostrar_roles()
                    break

    else:
        print("Todos los roles disponibles para crear ya están creados. Debes borrar alguno si quieres crear uno nuevo.")

def borrar_rol():
    print("¿Qué rol quieres borrar?")
    mostrar_roles()

    rol_a_borrar = None
    while True:
        rol_a_borrar = input("Rol a borrar -> ")
        if rol_a_borrar not in roles:
            print("El rol elegido no existe o ya ha sido borrado, elige uno válido.")
        else:
            break
    roles.remove(rol_a_borrar)
    print("Roles restantes")
    for i in roles:
        print("-", i)

def modificar_rol():
    print("¿Qué rol quieres modificar?")
    mostrar_roles()
    rol_a_modificar = None
    

    permisos = ("Consulta", "Edición", "Creación", "Borrado")
    permisos_si_no = [consulta, edicion, creacion, borrado]

    while True:
        rol_a_modificar = input("Rol a modificar -> ")
        if rol_a_modificar in roles:
            break
        else:
            print("El rol elegido no existe.")
    
    print("¿Qué va a poder hacer un " + rol_a_modificar + " a partir de ahora?")

    for i in range(len(permisos)):
        while True:
            permiso = input(permisos[i] + " (s/n) -> ")
            if permiso == "s":
                permisos_si_no[i] = True
                break
            elif permiso == "n":
                permisos_si_no[i] = False
                break
            else:
                print("La opción elegida no existe. Escribe s (si) o n (no)")

    if rol_a_modificar == "lector":
        Usuario.Usuario.lector["Consulta"] = permisos_si_no[0]
        Usuario.Usuario.lector["Edicion"] = permisos_si_no[1]
        Usuario.Usuario.lector["Creacion"] = permisos_si_no[2]
        Usuario.Usuario.lector["Borrado"] = permisos_si_no[3]
    elif rol_a_modificar == "editor":
        Usuario.Usuario.editor["Consulta"] = permisos_si_no[0]
        Usuario.Usuario.editor["Edicion"] = permisos_si_no[1]
        Usuario.Usuario.editor["Creacion"] = permisos_si_no[2]
        Usuario.Usuario.editor["Borrado"] = permisos_si_no[3]
    elif rol_a_modificar == "creador":
        Usuario.Usuario.creador["Consulta"] = permisos_si_no[0]
        Usuario.Usuario.creador["Edicion"] = permisos_si_no[1]
        Usuario.Usuario.creador["Creacion"] = permisos_si_no[2]
        Usuario.Usuario.creador["Borrado"] = permisos_si_no[3]
    else:
        Usuario.Usuario.admin["Consulta"] = permisos_si_no[0]
        Usuario.Usuario.admin["Edicion"] = permisos_si_no[1]
        Usuario.Usuario.admin["Creacion"] = permisos_si_no[2]
        Usuario.Usuario.admin["Borrado"] = permisos_si_no[3]

# EL PROGRAMA PRINCIPAL EMPIEZA AQUÍ

# Listamos las opciones con las que trabajar
tablas = ["Puntos de venta", "Videojuegos", "Generos", "Empresa",
          "Equipos", "Artistas", "Animadores", "Programadores", "Compositores"]

consulta = edicion = creacion = borrado = None # Variables que más tarde ayudarán a la modificación de los roles

# Creamos dos usuarios iniciales
admin_primero = Usuario.Usuario("admin", "Juan")
admin_primero.set_permisos_iniciales()

lector_primero = Usuario.Usuario("lector", "Juan 2.0")
lector_primero.set_permisos_iniciales()

usuarios.extend([admin_primero, lector_primero])

roles_predeterminados = ["lector", "editor", "creador", "admin"] # Establecemos los roles
roles = roles_predeterminados.copy()

print("Hola. Elige un usuario para empezar.")
mostrar_usuarios()
usuario = usuarios[usuario_existe() - 1]

decision_existe = False

while decision_existe == False:
    print("¿Quieres crear una tabla (a), trabajar con una ya existente (b) o tabajar con usuarios y roles (c)?")
    crear_trabajar_decision = input()

    if crear_trabajar_decision.lower() == "a":
        if usuario.puede_crear == True:
            crear_tabla()
        else:
            print("No se te permite crear tablas.")
            usuario.mostrar_permisos()
    elif crear_trabajar_decision.lower() == "b":
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

        # Una vez formateada la opción, damos opciones para trabajar con la tabla seleccionada
        # Si el usuario elige una opción no válida, seguiremos pidiendo hasta que de una correcta

        # El LECTOR puede CONSULTAR un registro
        # El EDITOR puede CONSULTAR, ELMINAR Y MODIFICAR un registro
        # El CREADOR puede CONSULTAR, AÑADIR, ELMINAR y MODIFICAR un registro
        # El ADMIN puede CONSULTAR, AÑADIR, ELMINAR y MODIFICAR un registro y BORRAR UNA TABLA
        opcion_valida = None
        while opcion_valida == None:
            print("¿Qué deseas hacer con '" + tabla_elegida +
                "', consultar (a), añadir (b), eliminar (c) o modificar (d) un registro, o bien, borrarla (e)?")
            eleccion = input()

            global op
            op = ["a) Ver toda la informacion", "b) Ver la información de un campo"]
            print("\nOpciones:")

            if eleccion == "a":
                if usuario.puede_consultar:
                    consultar_registro(tabla_elegida)
                    opcion_valida = True
                else:
                    print("No tienes permisos de consulta")
                    usuario.mostrar_permisos()
            elif eleccion == "b":
                if usuario.puede_crear:
                    anadir_registro(tabla_elegida)
                    opcion_valida = True
                else:
                    print("No tienes permisos de creación.")
                    usuario.mostrar_permisos()
            elif eleccion == "c":
                if usuario.puede_editar:
                    eliminar_registro(tabla_elegida)
                    opcion_valida = True
                else:
                    print("No tienes permisos de edicion.")
                    usuario.mostrar_permisos()
            elif eleccion == "d":
                if usuario.puede_editar:
                    modificar_registro(tabla_elegida)
                    opcion_valida = True
                else:
                    print("No tienes permisos de edicion.")
                    usuario.mostrar_permisos()
            elif eleccion == "e":
                if usuario.puede_borrar:
                    borrar_tabla(tabla_elegida)
                    opcion_valida = True
                else:
                    print("No tienes permisos de borrado.")
                    usuario.mostrar_permisos()
            else:
                print("La opción elegida no es válida. Elige una que sí lo sea.")
        
    elif crear_trabajar_decision.lower() == "c":
        preferencia_trabajo = None

        while True:
            print("En específico, ¿prefieres trabajar con usuarios (a) o roles (b)?")
            preferencia_trabajo = input()
            if preferencia_trabajo.lower() == "a":
                print("¿Deseas ver los usuarios existentes (a), crear uno nuevo (b), borrar (c) o modificar uno ya existente (d)?")
                decision_usuarios = input()
                if decision_usuarios.lower() == "a":
                    if usuario.puede_consultar:
                        mostrar_usuarios()
                        
                    else:
                        print("No tienes permisos de consulta.")
                elif decision_usuarios.lower() == "b":
                    if usuario.puede_crear:
                        crear_usuario()
                        
                    else:
                        print("No tienes permisos de creación.")
                elif decision_usuarios.lower() == "c":
                    if usuario.puede_borrar:
                        borrar_usuario()
                        
                    else:
                        print("No tienes permisos de borrado.")
                elif decision_usuarios.lower() == "d":
                    if usuario.puede_editar:
                        modificar_usuario()
                        
                    else:
                        print("No tienes permisos de edición.")
                else:
                    print("La opción elegida no es válida.")

            elif preferencia_trabajo.lower() == "b":
                print("¿Deseas ver los roles existentes (a), crear uno nuevo (b), borrar (c) o modificar uno ya existente (d)?")
                decision_roles = input()

                if decision_roles.lower() == "a":
                    if usuario.puede_consultar:
                        mostrar_roles()
                        
                    else:
                        print("No tienes permisos de consulta.")
                elif decision_roles.lower() == "b":
                    if usuario.puede_crear:
                        crear_rol()
                        
                    else:
                        print("No tienes permisos de creación.")
                elif decision_roles.lower() == "c":
                    if usuario.puede_borrar:
                        borrar_rol()
                        
                    else:
                        print("No tienes permisos de borrado.")
                elif decision_roles == "d":
                    if usuario.puede_editar:
                        modificar_rol()
                        
                    else:
                        print("No tienes permisos de edición.")
                else:
                    print("Opción elegida no válida.")
            else:
                print("Opción no válida.")
    else:
        print("La decisión elegida no es válida.")

    print("¿Deseas seguir operando con la base de datos o terminar tu actividad aquí? Inserta 's' si quieres continuar, de lo contrario, tu actividad se terminará.")
    seguir = input()

    if seguir != "s":
        decision_existe = True

print("Fin de la conexión.")