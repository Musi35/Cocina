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

        return cliente_data

    except Exception as e:
        print(f"Error al obtener cliente: {e}")
        return None

    finally:
        # Cerrar el cursor y la conexión
        if conex:
            cursor.close()
            conex.close()
            print("Conexión cerrada.")

def obtener_ruta(cliente_id):
    cliente_data = get_cliente(cliente_id)
    if cliente_data:
        ruta = f"src/AdminSoftware/res/img/costumers/{cliente_id}.png"
        return ruta
    else:
        return None

def obtener_nombre(cliente_id):
    cliente_data = get_cliente(cliente_id)
    if cliente_data:
        _, nombre, *_ = cliente_data
        return nombre
    else:
        return None

def obtener_ingredientes(cliente_id):
    cliente_data = get_cliente(cliente_id)
    if cliente_data:
        _, _, tomate, lechuga, cebolla, queso, _, _= cliente_data
        ingredientes = []

        if tomate:
            ingredientes.append("Tomate")
        if lechuga:
            ingredientes.append("Lechuga")
        if cebolla:
            ingredientes.append("Cebolla")
        if queso:
            ingredientes.append("Queso")

        return ingredientes
    else:
        return None

def obtener_refresco(cliente_id):
    cliente_data = get_cliente(cliente_id)
    if cliente_data:
        _, _, _, _, _, _, refresco, _ = cliente_data
        return refresco
    else:
        return None
