# importar libreria
import sqlite3

# crear la base de datos
conexion = sqlite3.connect("mibase.db")
cursor = conexion.cursor()
print(" paso por aqui")
# crear tabka
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios "\
           "(nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")

print("Creo la tabla")
conexion.commit()
conexion.close()


### otra manera de crear tablas
try:
    miconexion=sqlite3.connect("primerabd.db")
    cursor.execute("CREATE TABLE personal(nombre varchar(30), edad INTEGER, email VARCHAR(100)")
except Exception as ex:
    print(ex)    
