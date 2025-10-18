from conn import get_connection

def show_all_data():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT 
        s.student_id,
        s.student_name,
        c.course_id,
        c.course_name,
        t.teacher_id,
        t.teacher_name
    FROM ENROLLMENT e
    JOIN STUDENT s ON e.student_id = s.student_id
    JOIN COURSE c ON e.course_id = c.course_id
    JOIN TEACHER t ON c.teacher_id = t.teacher_id
    ORDER BY s.student_id;
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows
