import sqlite3

def connect():
    conn=sqlite3.connect("storage.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS storage (id INTEGER PRIMARY KEY, title text,username text,password text,url text);")
    conn.commit()
    conn.close

def add_entry(title, username, password, url):
    conn=sqlite3.connect("storage.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO storage VALUES (NULL, ?, ?, ?, ?)",(title, username, password, url))
    conn.commit()
    conn.close

def search_entry(title="", username="", password="", url=""):
    conn=sqlite3.connect("storage.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM storage WHERE title=? OR username=? or password=? or url=?",(title, username, password, url))
    rows=cur.fetchall()
    conn.close
    return rows


def edit_entry(id, title, username, password, url):
    conn=sqlite3.connect("storage.db")
    cur=conn.cursor()
    cur.execute("UPDATE storage SET title=?, username=?, password=?, url=?", (title, username, password, url))
    conn.commit()
    conn.close


def delete_entry(id):
    conn=sqlite3.connect("storage.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM storage WHERE id=?", (id,))
    conn.commit()
    conn.close()

def show_all():
    conn=sqlite3.connect("storage.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM storage")
    rows=cur.fetchall()
    conn.close
    return rows


