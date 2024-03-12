import psycopg2

# Parámetros de conexión a PostgreSQL
host = "localhost"
database = "burgers"
user = "postgres"
password = "a"

def connect():
    try:
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        print("Conexión exitosa")
        return connection
    except Exception as e:
        print(f"Error al conectar a PostgreSQL: {e}")
        return None

def get_cliente(cliente_id):
    # Establecer la conexión
    conex = connect()
    
    if not conex:
        return None

    try:
        # Crear un cursor para ejecutar consultas SQL
        cursor = conex.cursor()

        # Ejecutar la consulta
        cursor.execute("SELECT * FROM clientes WHERE id = %s;", (cliente_id,))
        
        # Obtener los resultados
        cliente_data = cursor.fetchone()

        if cliente_data:
            # Desempaquetar y devolver los datos individualmente
            id_cliente, nombre, tomate, lechuga, cebolla, queso, chesco = cliente_data
            return id_cliente, nombre, tomate, lechuga, cebolla, queso, chesco

        else:
            print(f"No se encontró cliente con ID {cliente_id}")
            return None

    except Exception as e:
        print(f"Error al obtener cliente: {e}")
        return None

    finally:
        # Cerrar el cursor y la conexión
        if conex:
            cursor.close()
            conex.close()
            print("Conexión cerrada.")
