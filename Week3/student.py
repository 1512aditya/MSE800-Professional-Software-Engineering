from conn import get_connection

def list_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM STUDENT")
    students = cursor.fetchall()
    conn.close()
    return students

def get_student_by_id(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM STUDENT WHERE student_id = ?", (student_id,))
    student = cursor.fetchone()
    
    cursor.execute("""
        SELECT c.course_name
        FROM ENROLLMENT e
        JOIN COURSE c ON e.course_id = c.course_id
        WHERE e.student_id = ?
    """, (student_id,))
    courses = cursor.fetchall()

    conn.close()
    return student, [c[0] for c in courses]
