from database import get_db

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
    res = conn.execute("SELECT * FROM equipos").fetchall()
    return [dict(row) for row in res]

def update_estado(id_equipo, estado):
    conn = get_db()
    conn.execute(
        "UPDATE equipos SET estado=? WHERE id=?",
        (estado, id_equipo)
    )
    conn.commit()
