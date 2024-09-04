import pymysql

def dame_conexion():
    return pymysql.connect(
        host='localhost',
        user='root',
        passwd='',
        db='dbflask'
    )

def insertar_articulo(nombre, precio):
    conexion = dame_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO articulos(nombre, precio) VALUES (%s, %s)", (nombre, precio))
        conexion.commit()
        conexion.close()

def listar_articulos():
    conexion = dame_conexion()
    articulos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre, precio FROM articulos")
        articulos = cursor.fetchall()
        conexion.close()
        return articulos

def eliminar_articulo(id):
    conexion = dame_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM articulos WHERE id = %s", (id))
        conexion.commit()
        conexion.close()
        
if __name__ == '__main__':
    # dame_conexion()
    articulos = listar_articulos()
    print(articulos)