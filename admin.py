import psycopg2

def readadmin():
    conn = psycopg2.connect(dbname="NikMate",user="postgres", password="Gwbis@99", host="localhost",port="5433")
    cur = conn.cursor()
    sql = "SELECT nama_admin, password_admin from admin"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data