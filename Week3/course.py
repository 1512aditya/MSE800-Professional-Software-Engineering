from conn import get_connection

def list_courses_with_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT s.student_name, c.course_name
        FROM ENROLLMENT e
        JOIN STUDENT s ON e.student_id = s.student_id
        JOIN COURSE c ON e.course_id = c.course_id
        ORDER BY c.course_name
    """)
    data = cursor.fetchall()
    conn.close()
    return data

def list_courses_with_teachers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.course_name, t.teacher_name
        FROM COURSE c
        JOIN TEACHER t ON c.teacher_id = t.teacher_id
        ORDER BY c.course_name
    """)
    data = cursor.fetchall()
    conn.close()
    return data
