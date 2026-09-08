import mysql.connector as mysql
import os
import dotenv
import csv

base_path = os.path.dirname(__file__)
my_path = os.path.dirname(base_path)
okulik_path = os.path.dirname(my_path)
lesson_path = os.path.dirname(okulik_path)
result_path = os.path.join(okulik_path, "eugene_okulik", 'Lesson_16', "hw_data", 'data.csv')

with open(result_path, newline='') as csv_file:
    file = csv.DictReader(csv_file)
    data = []
    for row in file:
        data.append(row)

dotenv.load_dotenv()
db = mysql.connect(
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSW"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    database=os.getenv("DB_NAME")
)

cursor = db.cursor(dictionary=True)
for student in data:
    cursor.execute("""
    SELECT
    s.group_id,
    s.id as student_id,
    g.title as group_title,
    b.title as book_title,
    m.value as mark_value,
    l.title as lesson_title,
    sub.title as subject_title
    FROM students s
    LEFT JOIN `groups` g ON g.id = s.group_id AND g.title = %s
    LEFT JOIN books b ON b.taken_by_student_id = s.id AND b.title = %s
    LEFT JOIN marks m ON m.student_id = s.id AND m.value = %s
    LEFT JOIN lessons l ON l.id = m.lesson_id AND l.title = %s
    LEFT JOIN subjects sub ON sub.id = l.subject_id AND sub.title = %s
    WHERE s.name = %s AND s.second_name = %s
    """,
                   (
                       student['group_title'],
                       student['book_title'],
                       student['mark_value'],
                       student['lesson_title'],
                       student['subject_title'],
                       student['name'],
                       student['second_name']
                   ))

    results = cursor.fetchall()

    if not results:
        print(f" В базе данных полностью отсутствует студент: {student['name']} {student['second_name']}")
        continue
    # lst = []
    #
    # for row in results:
    #     if row['group_title'] is not None:
    #         lst.append(row['group_title'])
    # print(lst)
    found_groups = [row['group_title'] for row in results if row['group_title'] is not None]
    found_books = [row['book_title'] for row in results if row['book_title'] is not None]
    found_subjects = [row['subject_title'] for row in results if row['subject_title'] is not None]
    found_lessons = [row['lesson_title'] for row in results if row['lesson_title'] is not None]
    found_marks = [row['mark_value'] for row in results if row['mark_value'] is not None]

    missing = []

    if not found_groups:
        missing.append(student['group_title'])
    if not found_books:
        missing.append(student['book_title'])
    if not found_subjects:
        missing.append(student['subject_title'])
    if not found_lessons:
        missing.append(student['lesson_title'])
    if not found_marks:
        missing.append(student['mark_value'])

    missing_str = ',\n'.join(missing)
    if missing:
        # print(f"Студент - 'Имя': '{student['name']}', 'Фамилия': '{student['second_name']}',"
        #       f" не хватает в базе: '{'\n'.join(missing)}'")
        print(f"Студент - 'Имя': '{student['name']}', 'Фамилия': '{student['second_name']}',"
              f" не хватает в базе: '{missing_str}'")
