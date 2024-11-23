import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="abc123.",
        database="instituto"
    )

    cursor = conexion.cursor()

    sentencia = """INSERT INTO alumnos (nombre, apellidos, correo_e, fecha_nacimiento) 
                    VALUES (%s, %s, %s, %s)"""

    valores = [
        ("Juan", "García López", "juan.garcia@hotmail.es", "1998-10-10"),
        ("María", "Fernández Gómez", "mfernandez@yahoo.com", "1999-11-11"),
        ("Lucía", "González Sánchez", "luciags@gmail.com", "2000-12-12")
    ]

    cursor.executemany(sentencia, valores)

    conexion.commit()

    print(cursor.rowcount, "registros insertados.")
    conexion.close()
except mysql.connector.Error as error:
    print("Error de MySQL:", error)