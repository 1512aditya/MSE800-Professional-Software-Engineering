from conn import get_connection

def list_teachers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM TEACHER")
    teachers = cursor.fetchall()
    conn.close()
    return teachers
