import mysql.connector
import random

hosts = "containers-us-west-95.railway.app"
users = "root"
ports = "6640"
passwords = "tkC2gwluqGqMls9ZOHvY"

mydb = mysql.connector.connect(
  host=hosts,
  user=users,
  port=ports,
  password=passwords,
  database="videojuegos"
)
my_cursor = mydb.cursor()

# Quedan los distintos tipos de empleado

# Generador aleatorio DNIs
nums = "1234567890"
letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
dni = ""

dni_list = []

for i in range(32):
    dni = ""
    for i in range(8):
        dni += nums[random.randint(0, len(nums) - 1)]
    dni += letters[random.randint(0, len(letters) - 1)]
    dni_list.append(dni)

# print(dni_list)
# print(len(dni_list))


# Nombre e email C:

termination = "@gmail.com"
emails = []

txt = open("/Users/kevs/Documents/ncompositores.txt", mode="r")
names = []
with txt as nombres:
  emails = []
  for nombre in nombres:
    names.append(nombre.replace("\n", ""))
    emails.append((nombre.replace("\n", "") + termination).lower()) # Para los emails, quitamos el '\n', añadimos terminacion y lo pasamos a minúscula

# print("\n", names)
# print(emails)
txt.close()

# Equipos
c = 1
equipos = []
for i in range(16):
  for j in range(2):
    equipos.append(c)
  c +=1

#print(equipos)

# Generador aleatorio de cps
cp = ""
cps = []

for i in range(32):
  cp = ""
  for i in range(5):
    cp += nums[random.randint(0, len(nums) - 1)]
  cps.append(cp)
#print(cps)

# 32 poblaciones distintas
# Las 32 poblacions que se insertan aleatoriamente se corresponden con una provincia
pob_prov = {
  "El Martillar": "Valencia",
  "Casillar": "Madrid",
  "El Escorial": "Madrid",
  "Corollos": "Asturias",
  "Astricas": "Andalucía",
  "Cantes": "Andalucía",
  "Pasquet": "Navarra",
  "Zedpas": "Galicia"
}

pob = [] # Poblaciones diferentes
for i in pob_prov.keys():
  pob.append(i)

poblaciones = [] # 32 poblaciones
for i in range(32):
  poblaciones.append(pob[random.randint(0, 7)])

provincias = []
for i in poblaciones:
  provincias.append(pob_prov[i])

#print(poblaciones, "\n", provincias)

# designador de experiencia aleatoria
exp = []

for i in range(32):
  exp.append(str(random.randint(1, 10)) + " años")
#print("\n", exp)

# Formación compositores
f = ["Técnico en Video DJ y Sonido", "Máster en Producción Musical", "Máster en ingeniería de sonido", 
"Técnico superior en sonido para audiovisuales y espectáculos"]

f_compositores = []
for i in range(32):
  f_compositores.append(f[random.randint(0, 3)])

# Generador de sueldo aleatorio
sueldos = []
for i in range(32):
  sueldos.append(random.randint(20000, 40000))
#print(sueldos) 

ids = 1
#dni = ["12345678A", "89421568B", "12789654A", "22547880S", "02014749F", "98698569Z", "30650478Q", "98856970W", "87654321AAA", "21589452B", "00023208C", "23012320D", "74182963A", "45120010E", "96832960H", "26780800I"]
# nombre = []
# email = []
# equipo = []
# cp = []
# poblacion = []
# provincia = []
# experiencia = []
# formacion = []
# sueldo = []

for i in range(32):
  sql = "INSERT INTO compositores VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
  val = (ids, dni_list[i], names[i], emails[i], equipos[i], cps[i], poblaciones[i], provincias[i], exp[i], 
  f_compositores[i], sueldos[i])

  my_cursor.execute(sql, val)
  ids += 1

mydb.commit()

my_cursor.execute("SELECT * FROM compositores")
my_result = my_cursor.fetchall()

for i in my_result:
  print(i)
