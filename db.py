import pymysql

def establecer_conexion():
    return pymysql.connect(
        host='localhost',
        user='root',
        passwd='',
        db='dbflask'
    )

def insertar_articulo(nombre, precio):
    try:
        conexion = establecer_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO articulos(nombre, precio) VALUES (%s, %s)", (nombre, precio))
            conexion.commit()
            conexion.close()
    except Exception as e:
        print(f'Error al conectar a la base de datos: {e}')

def listar_articulos():
    conexion = establecer_conexion()
    articulos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre, precio FROM articulos")
        articulos = cursor.fetchall()
        conexion.close()
        return articulos

def eliminar_articulo(id):
    conexion = establecer_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM articulos WHERE id = %s", (id))
        conexion.commit()
        conexion.close()
        
def obtener_articulo(id):
    conexion = establecer_conexion()
    articulo = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre, precio FROM articulos WHERE id = %s", (id))
        articulo = cursor.fetchone()
        conexion.close()
        return articulo

def actualizar_articulo(id, nombre, precio):
    conexion = establecer_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE articulos SET nombre = %s, precio = %s WHERE id = %s", (nombre, precio, id))
        conexion.commit()
        conexion.close()

# if __name__ == '__main__':
#     alta_usuario('jluna@mail.com', 'password')
#     print(obtener_usuario('jluna@mail.com')[1])
