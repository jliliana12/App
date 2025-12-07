import sqlite3
import os

DB_NAME = os.path.join(os.path.dirname(__file__), "equipos.db")

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if not os.path.exists(DB_NAME):
        conn = get_db()
        conn.execute("""
            CREATE TABLE IF NOT EXISTS equipos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo TEXT,
                modelo TEXT,
                estado TEXT,
                fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        conn.close()

def create_equipo(tipo, modelo, estado):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO equipos(tipo, modelo, estado) VALUES (?, ?, ?)",
                (tipo, modelo, estado))
    conn.commit()
    conn.close()
    return cur.lastrowid

def get_all():
    conn = get_db()
    rows = conn.execute("SELECT * FROM equipos ORDER BY fecha DESC").fetchall()
    conn.close()
    return [dict(r) for r in rows]

def update_estado(id_equipo, estado):
    conn = get_db()
    conn.execute("UPDATE equipos SET estado=? WHERE id=?", (estado, id_equipo))
    conn.commit()
    conn.close()
