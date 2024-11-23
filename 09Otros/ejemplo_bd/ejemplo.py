import mysql.connector

# Conexión a la base de datos

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="abc123.",
        database="instituto"
    )

    cursor = conexion.cursor(dictionary=True)

    # Consulta a la base de datos

    sentencia = "SELECT * FROM alumnos"

    cursor.execute(sentencia)

    # Recuperación de los resultados

    resultados = cursor.fetchall()

    for alumno in resultados:
        print("Nombre:", alumno["nombre"])
        print("Apellidos:", alumno["apellidos"])
        print("Correo-e:", alumno["correo_e"])
        
    conexion.close()
except mysql.connector.Error as error:
    print("Error de MySQL:", error)
