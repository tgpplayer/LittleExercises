# Roles: lector (consultar), editor (consultar y editar), creador(consultar, editar y crear)
# y admin (consultar, editar, crear y borrar)
import Usuario

consulta = edicion = creacion = borrado = None

admin_primero = Usuario.Usuario("admin", "Juan")
admin_primero.set_permisos_iniciales()

lector_primero = Usuario.Usuario("lector", "Juan 2.0")
lector_primero.set_permisos_iniciales()

usuarios = []
roles_predeterminados = ["lector", "editor", "creador", "admin"]
roles = roles_predeterminados.copy()

usuarios.append(admin_primero)
print(len(usuarios))

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
    if len(roles) < 4:
        print("¿Qué rol quieres crear?")
        mostrar_roles()
        rol_a_crear = None
        while True:
            rol_a_crear = input("Rol a crear -> ")
            print(roles_predeterminados)
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

# borrar_rol()
# crear_rol()
modificar_rol()

crear_usuario()
borrar_usuario()
modificar_usuario()
crear_usuario()
borrar_usuario()