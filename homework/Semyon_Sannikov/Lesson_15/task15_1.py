import mysql.connector as mysql


db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)
cursor = db.cursor(dictionary=True)


def insert_student(db_cursor, name, second_name):
    query = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
    db_cursor.execute(query, (name, second_name))
    return db_cursor.lastrowid


def insert_group(db_cursor, title, start_date, end_date):
    query = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
    db_cursor.execute(query, (title, start_date, end_date))
    return db_cursor.lastrowid


def insert_book(db_cursor, title, target_student_id):
    query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
    db_cursor.execute(query, (title, target_student_id))
    return db_cursor.lastrowid


def insert_subject(db_cursor, title):
    query = "INSERT INTO subjects (title) VALUES (%s)"
    db_cursor.execute(query, (title,))
    return db_cursor.lastrowid


def insert_lesson(db_cursor, title, subject_id):
    query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
    db_cursor.execute(query, (title, subject_id))
    return db_cursor.lastrowid


def insert_mark(db_cursor, value, lesson_id, target_student_id):
    query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
    db_cursor.execute(query, (value, lesson_id, target_student_id))
    return db_cursor.lastrowid


student_id = insert_student(cursor, 'Mister', 'Defov')

group_id = insert_group(cursor, 'Def_test_finish', 'march_2025', 'march_2026')

book1_id = insert_book(cursor, 'Azbuka RED', student_id)
book2_id = insert_book(cursor, 'Azbuka BLUE', student_id)

add_student = "UPDATE students SET group_id = %s where id = %s"
cursor.execute(add_student, (group_id, student_id))

subject1_id = insert_subject(cursor, 'Химия')
subject2_id = insert_subject(cursor, 'Биология')

lesson1_id = insert_lesson(cursor, 'Semyon_Lessons_14', subject1_id)
lesson2_id = insert_lesson(cursor, 'Semyon_Lessons_15', subject2_id)

mark1_id = insert_mark(cursor, 2, lesson1_id, student_id)
mark2_id = insert_mark(cursor, 3, lesson2_id, student_id)

select_query_marks = """
SELECT name, second_name, value from students
join marks
on students.id = marks.student_id
and students.id = %s
"""
cursor.execute(select_query_marks, (student_id,))
print(cursor.fetchall())

select_query_books = """
SELECT name, second_name, title from students
join books
on students.id = books.taken_by_student_id
and books.taken_by_student_id = %s
"""
cursor.execute(select_query_books, (student_id,))
print(cursor.fetchall())

student_query = """
SELECT s.name as name,
s.second_name as second_name,
g.title as groups_title,
b.title as book_title,
m.value as value,
l.title as lesson_title,
sub.title as subject_title
FROM students s
LEFT JOIN `groups` g on s.group_id = g.id
LEFT JOIN books b ON s.id = b.taken_by_student_id
LEFT JOIN marks m ON s.id = m.student_id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjects sub ON l.subject_id = sub.id
where s.id = %s
"""
cursor.execute(student_query, (student_id,))
print(cursor.fetchall())

db.commit()
db.close()
