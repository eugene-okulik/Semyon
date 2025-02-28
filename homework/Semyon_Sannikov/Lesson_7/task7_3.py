result1 = 'результат операции: 42'
result2 = 'результат операции: 54'
result_work = 'результат работы программы: 209'
result3 = 'результат: 2'

def otvet(result):
    subsctring = int(result.split()[-1])
    while True:
        result = subsctring
        print(result + 10)
        break

otvet(result1)
otvet(result2)
otvet(result_work)
otvet(result3)
