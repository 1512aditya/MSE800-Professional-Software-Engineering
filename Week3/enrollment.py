from conn import get_connection

def list_enrollments():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT s.student_name, c.course_name
        FROM ENROLLMENT e
        JOIN STUDENT s ON e.student_id = s.student_id
        JOIN COURSE c ON e.course_id = c.course_id
    """)
    enrollments = cursor.fetchall()
    conn.close()
    return enrollments
