# Roles: lector (consultar), editor (consultar y editar), creador(consultar, editar y crear)
# y admin (consultar, editar, crear y borrar)

class Usuario:
  nick = None
  rol = None
  puede_consultar = False
  puede_editar = False
  puede_crear = False
  puede_borrar = False

  lector = {
    "Consulta": True,
    "Edicion": False,
    "Creacion": False,
    "Borrado": False
  }
  editor = {
      "Consulta": True,
      "Edicion": True,
      "Creacion": False,
      "Borrado": False
  }
  creador = {
      "Consulta": True,
      "Edicion": True,
      "Creacion": True,
      "Borrado": False
  }
  admin = {
      "Consulta": True,
      "Edicion": True,
      "Creacion": True,
      "Borrado": True
  }

  def __init__(self, rol, nick):
    self.rol = rol
    self.nick = nick

  def set_permisos_iniciales(self):
    if self.rol == "lector":
      self.puede_consultar = self.lector["Consulta"]
      self.puede_editar = self.lector["Edicion"]
      self.puede_crear = self.lector["Creacion"]
      self.puede_borrar = self.lector["Borrado"]
    elif self.rol == "editor":
      self.puede_consultar = self.editor["Consulta"]
      self.puede_editar = self.editor["Edicion"]
      self.puede_crear = self.editor["Creacion"]
      self.puede_borrar = self.editor["Borrado"]
    elif self.rol == "creador":
      self.puede_consultar = self.creador["Consulta"]
      self.puede_editar = self.creador["Edicion"]
      self.puede_crear = self.creador["Creacion"]
      self.puede_borrar = self.creador["Borrado"]
    else:
      self.puede_consultar = self.admin["Consulta"]
      self.puede_editar = self.admin["Edicion"]
      self.puede_crear = self.admin["Creacion"]
      self.puede_borrar = self.admin["Borrado"]
    
  def set_permisos_nuevos(self):
    print("¿Qué premisos quieres darle a este " + self.rol + " ?")
    si_o_no = " (s/n)"
    
    while True:
      permiso = input("Consulta " + si_o_no + " -> ")
      if permiso == "s":
        self.puede_consultar = True
        break
      elif permiso == "n":
        self.puede_consultar = False
        break
      else:
        print("Opción no válida, escribe s (si) o n (no)")

    while True:
      permiso = input("Edición " + si_o_no + " -> ")
      if permiso == "s":
        self.puede_editar = True
        break
      elif permiso == "n":
        self.puede_editar = False
        break
      else:
        print("Opción no válida, escribe s (si) o n (no)")

    while True:
      permiso = input("Creación " + si_o_no + " -> ")
      if permiso == "s":
        self.puede_crear = True
        break
      elif permiso == "n":
        self.puede_crear = False
        break
      else:
        print("Opción no válida, escribe s (si) o n (no)")
    
    while True:
      permiso = input("Borrado " + si_o_no + " -> ")
      if permiso == "s":
        self.puede_borrar = True
        break
      elif permiso == "n":
        self.puede_borrar = False
        break
      else:
        print("Opción no válida, escribe s (si) o n (no)")


  def mostrar_permisos(self):
    print("Permisos del usuario:")
    if self.puede_consultar:
        print("- puede consultar")
    if self.puede_editar:
        print("- puede editar")
    if self.puede_crear:
        print("- puede crear")
    if self.puede_borrar:
        print("- puede borrar")