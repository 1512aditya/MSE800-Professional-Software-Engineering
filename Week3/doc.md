
---

# 📘 YOOBEE College Database Project

## 📌 Project Overview

This project implements a **SQLite3 database** to efficiently manage academic information for a college.
It tracks:

* **Students** and their details
* **Teachers** and the courses they teach
* **Courses** taught at the college
* **Enrollments** of students into courses

---

## 📂 Project Structure

```
yoobee_college/
│
├── main.py          # Entry point (menu system to run the program)
├── db_setup.py      # Creates database tables and fills them with sample data
├── utils.py         # Database connection utility
├── student.py       # Queries related to students
├── teacher.py       # Queries related to teachers
├── course.py        # Queries related to courses
├── enrollment.py    # Queries related to enrollments
├── report.py        # Cross-table queries (full joined reports)
└── README.md        # Documentation (this file)
```

---

## ⚙️ Database Schema

### **STUDENT**

* `student_id` (PK)
* `student_name`

### **TEACHER**

* `teacher_id` (PK)
* `teacher_name`

### **COURSE**

* `course_id` (PK)
* `course_name`
* `teacher_id` (FK → TEACHER)

### **ENROLLMENT**

* `student_id` (FK → STUDENT)
* `course_id` (FK → COURSE)
* Composite PK (`student_id`, `course_id`)

---

## 📜 Files Explained

### **utils.py**

Contains helper to connect to SQLite database:

```python
def get_connection():
    return sqlite3.connect("YBCOLLEGE.db")
```

---

### **database.py**

* Drops old tables (if exist).
* Creates `STUDENT`, `TEACHER`, `COURSE`, `ENROLLMENT`.
* Inserts **manual sample data** (10 students, 10 teachers, 10 courses, 20 enrollments).

Run once automatically by `main.py`.

---

### **student.py**

* **List all students**
* **Search by student\_id** and show their enrolled courses:

```sql
SELECT * FROM STUDENT WHERE student_id = ?;
SELECT c.course_name
FROM ENROLLMENT e
JOIN COURSE c ON e.course_id = c.course_id
WHERE e.student_id = ?;
```

---

### **teacher.py**

* List all teachers in the database.

---

### **course.py**

* **List which student is enrolled in which course**:

```sql
SELECT s.student_name, c.course_name
FROM ENROLLMENT e
JOIN STUDENT s ON e.student_id = s.student_id
JOIN COURSE c ON e.course_id = c.course_id;
```

* **List which teacher is connected to which course**:

```sql
SELECT c.course_name, t.teacher_name
FROM COURSE c
JOIN TEACHER t ON c.teacher_id = t.teacher_id;
```

---

### **enrollment.py**

Handles enrollment-specific queries (student ↔ course links).

---

### **report.py**

Cross-table reporting:

* Shows **student, course, teacher** all in one row:

```sql
SELECT 
    s.student_id, s.student_name,
    c.course_id, c.course_name,
    t.teacher_id, t.teacher_name
FROM ENROLLMENT e
JOIN STUDENT s ON e.student_id = s.student_id
JOIN COURSE c ON e.course_id = c.course_id
JOIN TEACHER t ON c.teacher_id = t.teacher_id
ORDER BY s.student_id;
```

---

### **main.py**

The entry point with a **menu-driven system**.

Menu options:

1. Show which student is enrolled in which course
2. Show which teacher is connected to which course
3. Search a student by ID
4. Exit
   (Optionally, you can extend with **5: Full report** using `report.py`)

Example interaction:

```
--- YOOBEE COLLEGE MENU ---
1: Which student is enrolled in which course
2: Which teacher is connected to which course
3: Search a student by ID
4: FULL DATA REPORT
5: Exit
Enter your choice: 1
```

---

## ▶️ How to Run

1. Clone/download the project folder.
2. Run in terminal:

```bash
python main.py
```

3. Database `YBCOLLEGE.db` will be created automatically with sample data.
4. Use the menu to interact with data.

---

## 📊 Example Outputs

**Option 1 (Students ↔ Courses):**

```
John Carter → Computer Science 101
John Carter → Database Systems
Sophia Williams → Data Structures
Sophia Williams → Artificial Intelligence
...
```

**Option 2 (Teachers ↔ Courses):**

```
Dr. Alice Johnson teaches Computer Science 101
Prof. Brian Smith teaches Database Systems
...
```

**Option 3 (Search Student by ID):**

```
Enter Student ID: 5
Student ID: 5
Name: Noah Anderson
Enrolled Courses: Computer Networks, Database Systems
```

**Option 5 (Full Report – from report.py):**

```
(1, 'John Carter', 1, 'Computer Science 101', 1, 'Dr. Alice Johnson')
(1, 'John Carter', 2, 'Database Systems', 2, 'Prof. Brian Smith')
...
```

---