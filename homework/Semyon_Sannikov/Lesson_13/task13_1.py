import os
from datetime import datetime, timedelta


base_path = os.path.dirname(__file__)
my_path = os.path.dirname(base_path)
okulik_path = os.path.dirname(my_path)
result_path = os.path.join(okulik_path, "eugene_okulik", 'hw_13', 'data.txt')


def view_file():
    with open(result_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            yield line


file_generator = view_file()
first_line = next(file_generator)
second_line = next(file_generator)
third_line = next(file_generator)


def extract_time(line):
    line_without_number = line.split('. ', 1)[1]
    time_part = line_without_number.split(' - ')[0]
    dt = datetime.strptime(time_part, '%Y-%m-%d %H:%M:%S.%f')
    return dt


week = extract_time(first_line)
after_week = week + timedelta(days=7)
week_day = extract_time(second_line).strftime('%A')
now_day = datetime.now() - extract_time(third_line)
print(after_week)
print(week_day)
print(now_day.days)
