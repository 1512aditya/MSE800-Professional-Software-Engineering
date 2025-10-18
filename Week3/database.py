from conn import get_connection

def setup_database():
    conn = get_connection()
    cursor = conn.cursor()

    # Drop tables if they exist
    cursor.execute("DROP TABLE IF EXISTS ENROLLMENT")
    cursor.execute("DROP TABLE IF EXISTS COURSE")
    cursor.execute("DROP TABLE IF EXISTS STUDENT")
    cursor.execute("DROP TABLE IF EXISTS TEACHER")

    # Create TEACHER table
    cursor.execute("""
    CREATE TABLE TEACHER (
        teacher_id INTEGER PRIMARY KEY,
        teacher_name TEXT NOT NULL
    )
    """)

    # Create STUDENT table
    cursor.execute("""
    CREATE TABLE STUDENT (
        student_id INTEGER PRIMARY KEY,
        student_name TEXT NOT NULL
    )
    """)

    # Create COURSE table
    cursor.execute("""
    CREATE TABLE COURSE (
        course_id INTEGER PRIMARY KEY,
        course_name TEXT NOT NULL,
        teacher_id INTEGER NOT NULL,
        FOREIGN KEY (teacher_id) REFERENCES TEACHER(teacher_id)
    )
    """)

    # Create ENROLLMENT table
    cursor.execute("""
    CREATE TABLE ENROLLMENT (
        student_id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        PRIMARY KEY (student_id, course_id),
        FOREIGN KEY (student_id) REFERENCES STUDENT(student_id),
        FOREIGN KEY (course_id) REFERENCES COURSE(course_id)
    )
    """)

    # ------------------------
    # Insert TEACHERS
    # ------------------------
    teachers = [
        (1, "Prof. Alice Johnson"),
        (2, "Prof. Brian Smith"),
        (3, "Prof. Catherine Green"),
        (4, "Prof. Daniel White"),
        (5, "Prof. Emily Brown"),
        (6, "Prof. Frank Wilson"),
        (7, "Prof. Grace Taylor"),
        (8, "Prof. Henry Lee"),
        (9, "Prof. Irene Davis"),
        (10, "Prof. Jack Miller")
    ]
    cursor.executemany("INSERT INTO TEACHER VALUES (?, ?)", teachers)

    # ------------------------
    # Insert STUDENTS
    # ------------------------
    students = [
        (1, "Aditya Maisuriya"),
        (2, "Sophia Williams"),
        (3, "Liam Johnson"),
        (4, "Olivia Martinez"),
        (5, "Noah Anderson"),
        (6, "Emma Thompson"),
        (7, "James Robinson"),
        (8, "Isabella Clark"),
        (9, "Mason Lewis"),
        (10, "Mia Walker")
    ]
    cursor.executemany("INSERT INTO STUDENT VALUES (?, ?)", students)

   
    courses = [
        (1, "Research Methods", 1),
        (2, "Database Systems", 2),
        (3, "Data Structures", 3),
        (4, "Artificial Intelligence", 4),
        (5, "Software Engineering", 5),
        (6, "Quantam Computing", 6),
        (7, "Operating Systems", 7),
        (8, "Computer Networks", 8),
        (9, "Machine Learning", 9),
        (10, "Web Development", 10)
    ]
    cursor.executemany("INSERT INTO COURSE VALUES (?, ?, ?)", courses)

    enrollments = [
        (1, 1), (1, 2),
        (2, 3), (2, 4),
        (3, 5), (3, 1),
        (4, 6), (4, 7),
        (5, 8), (5, 2),
        (6, 9), (6, 3),
        (7, 10), (7, 4),
        (8, 5), (8, 6),
        (9, 7), (9, 8),
        (10, 9), (10, 10)
    ]
    cursor.executemany("INSERT INTO ENROLLMENT VALUES (?, ?)", enrollments)

    conn.commit()
    conn.close()
    print("Database setup complete with manual sample data!")
