result1 = 'результат операции: 42'
result2 = 'результат операции: 514'
result_work = 'результат работы программы: 9'

my_result1 = ((result1.index(': ')) + 1)
my_result1 = int(result1[my_result1:]) + 10
print(my_result1)

my_result2 = ((result2.index(': ')) + 1)
my_result2 = int(result2[my_result2:]) + 10
print(my_result2)

my_result_work = ((result_work.index(': ')) + 1)
my_result_work = int(result_work[my_result_work:]) + 10
print(my_result_work)
