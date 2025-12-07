from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave-segura'
DB_NAME = "equipos.db"


def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS equipos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            serie TEXT,
            estado TEXT,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def create_equipo(nombre, serie, estado):
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO equipos(nombre, serie, estado) VALUES (?, ?, ?)",
        (nombre, serie, estado)
    )
    conn.commit()
    return cur.lastrowid

def get_equipo(id_equipo):
    conn = get_db()
    res = conn.execute("SELECT * FROM equipos WHERE id=?", (id_equipo,)).fetchone()
    return dict(res) if res else None

def get_all():
    conn = get_db()
    rows = conn.execute("SELECT * FROM equipos").fetchall()
    return [dict(r) for r in rows]

def update_estado(id_equipo, estado):
    conn = get_db()
    conn.execute("UPDATE equipos SET estado=? WHERE id=?", (estado, id_equipo))
    conn.commit()


@app.route("/")
def index():
    equipos = get_all()
    return render_template("index.html", equipos=equipos)

@app.route("/registrar", methods=["GET", "POST"])
def registrar():
    if request.method == "POST":
        nombre = request.form["nombre"]
        serie = request.form["serie"]
        estado = request.form["estado"]
        create_equipo(nombre, serie, estado)
        return redirect(url_for("index"))
    return render_template("registrar.html")

@app.route("/actualizar_estado")
def actualizar_estado():
    return render_template("actualizar_estado.html")

@app.route("/historial")
def historial():
    equipos = get_all()
    return render_template("historial.html", equipos=equipos)

@app.route("/alertas")
def alertas():
    return render_template("alertas.html")

@app.route("/informes")
def informes():
    return render_template("informes.html")


if __name__ == "__main__":
    init_db()


    if os.name == "nt":
       
        from waitress import serve
        serve(app, host="0.0.0.0", port=8080)

    else:
        
        app.run(debug=True, host="0.0.0.0", port=8080)