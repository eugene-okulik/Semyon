import datetime
task_time = 'Jan 15, 2023 - 12:05:33'

python_date = datetime.datetime.strptime(task_time, '%b %d, %Y - %H:%M:%S')
full_time = python_date.strftime('%B')
format_date = python_date.strftime('%d.%m.%Y, %H:%M')

print(full_time)
print(format_date)
