import mysql.connector


try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="abc123.",
        database="instituto"
    )

    cursor = conexion.cursor()

    # Consulta a la base de datos

    sentencia = "SELECT * FROM alumnos"

    cursor.execute(sentencia)

    # Recuperación de los resultados

    resultados = cursor.fetchall()

    for alumno in resultados:
        print("Nombre:", alumno[0])
        print("Apellidos:", alumno[1])
        print("Correo-e:", alumno[2])

    conexion.close()
except mysql.connector.Error as error:
    print("Error de MySQL:", error)