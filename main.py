from flask import Flask, redirect, url_for, render_template, request
import db

app = Flask(__name__)

@app.route('/agregar_articulo')
def agregar_articulo():
    return render_template('agregar_articulo.html')

@app.route('/guardar_articulo', methods=['POST'])
def guardar_articulo():
    nombre = request.form['nombre']
    precio = request.form['precio']
    try:
        db.insertar_articulo(nombre, precio)
    except Exception as e:
        print(f'Ha ocurrido un error al insertar el articulo: {e}')
    finally:
        return redirect('/articulos')

@app.route('/')
@app.route('/articulos')
def articulos():
    articulos = db.listar_articulos()
    return render_template('articulos.html', articulos=articulos)

@app.route('/eliminar_articulo', methods=['POST'])
def eliminar_articulo():
    db.eliminar_articulo(request.form['id'])
    return redirect('/articulos')

@app.route('/editar_articulo/<int:id>')
def editar_articulo(id):
    articulo = db.obtener_articulo(id)
    return render_template('editar_articulo.html', articulo=articulo)

@app.route('/actualizar_articulo', methods=['POST'])
def actualizar_articulo():
    id = request.form['id']
    nombre = request.form['nombre']
    precio = request.form['precio']
    db.actualizar_articulo(id, nombre, precio)
    return redirect('/articulos')

if __name__ == '__main__':
    app.run(debug=True)