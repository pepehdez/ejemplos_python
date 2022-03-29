import sqlite3
#

miConexion = sqlite3.connect("udc.db")

try:
    miConexion.execute("""
                    CREATE TABLE deportistas( 
                     ID interge primary autoincrement,
                     NOMBRE text,
                     EDAD interge,
                     PESO real,
                     TALLA real,
                     IMC real
                    ) 
                """)
    print("CONEXION", "Base de datos creada exitosamente")
except sqlite3.OperationalError:
    print("CONEXION", "Conectada exitosa con la base de datos")
    miConexion.close()

# Eliminar la base de datos
    
   